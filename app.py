"""
app.py
------
This is the Streamlit web app for the AI eLearning Course Generator.
It provides a simple UI where anyone can:
1. Upload a PDF file
2. Click "Run Pipeline"
3. See the generated screens and titles

Run it with: streamlit run app.py
"""

import streamlit as st
import tempfile
import os
from e2e_test import build_storyboard

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI eLearning Generator",
    page_icon="🤖",
    layout="centered"
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🤖 AI eLearning Course Generator")
st.markdown("Upload a PDF and automatically generate a complete eLearning storyboard using local AI.")
st.divider()

# ── File Upload ───────────────────────────────────────────────────────────────
st.subheader("📄 Step 1: Upload your PDF")
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    help="Upload any PDF document to generate an eLearning course from it."
)

# ── Run Button ────────────────────────────────────────────────────────────────
st.subheader("▶️ Step 2: Run the Pipeline")
run_button = st.button("🚀 Generate Course", type="primary", use_container_width=True)

# ── Pipeline Logic ────────────────────────────────────────────────────────────
if run_button:
    # Check if a file was uploaded
    if uploaded_file is None:
        st.error("❌ Please upload a PDF file first!")
    else:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Show a progress message while generating
        with st.spinner("🧠 AI is generating your course... This may take a few minutes."):
            try:
                # Run the full pipeline
                storyboard = build_storyboard(tmp_path)

                # ── Results ───────────────────────────────────────────────
                st.divider()
                st.subheader("✅ Step 3: Results")

                # Show total screen count
                st.success(f"🎉 {len(storyboard)} screens generated successfully!")

                # Show summary metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Screens", len(storyboard))
                col2.metric("Content Screens", sum(1 for s in storyboard if s["type"] == "screen"))
                col3.metric("Quiz Questions", sum(1 for s in storyboard if s["type"] == "cyu"))

                st.divider()

                # Show all screen titles
                st.subheader("📋 Generated Screens")

                # Colour mapping for screen types
                type_colors = {
                    "introduction": "🔵",
                    "objectives":   "🟣",
                    "screen":       "🟢",
                    "cyu":          "🟠",
                    "summary":      "🟡",
                }

                for i, screen in enumerate(storyboard, 1):
                    stype = screen["type"]
                    title = screen["title"]
                    emoji = type_colors.get(stype, "⚪")

                    # Show each screen as an expandable section
                    with st.expander(f"{i}. {emoji} [{stype.upper()}] {title}"):
                        if stype == "cyu":
                            st.write(f"**Question:** {screen.get('question', '')}")
                            options = screen.get("options", {})
                            correct = screen.get("correct_answer", "")
                            for key, val in options.items():
                                tick = " ✓" if key == correct else ""
                                st.write(f"{key}) {val}{tick}")
                            st.write(f"**Correct Answer:** {correct}")
                        else:
                            st.write(screen.get("content", ""))

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
            finally:
                # Clean up the temporary file
                os.unlink(tmp_path)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Python, Ollama & Streamlit — Mediant Labs Internship 2026")
