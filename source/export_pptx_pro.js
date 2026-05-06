const pptxgen = require("pptxgenjs");

// ── Palette: Midnight Executive ──────────────────────────────────────────────
const C = {
  navy:    "1E2761",
  ice:     "CADCFC",
  white:   "FFFFFF",
  dark:    "0F1640",
  mid:     "2E3F8F",
  accent:  "5B8CFF",
  green:   "2ECC71",
  orange:  "E67E22",
  text:    "1A1A2E",
  muted:   "8892B0",
};

// ── Storyboard data ──────────────────────────────────────────────────────────
const storyboard = [
  {
    type: "introduction",
    title: "Introduction",
    content: "Artificial Intelligence (AI) is a rapidly evolving field of computer science that seeks to replicate human intelligence through intelligent machines. It enables learning, reasoning, and problem-solving — shifting from rule-based systems to machine learning and deep learning. AI is transforming healthcare, education, transportation, and finance, while raising critical ethical concerns around privacy, bias, and responsibility. Responsible development and ethical frameworks are key to harnessing AI's power safely."
  },
  {
    type: "objectives",
    title: "Learning Objectives",
    objectives: [
      "Define Artificial Intelligence and its role in computer science",
      "Distinguish between Narrow AI and General AI",
      "Understand machine learning as the core subset of AI",
      "Explain deep learning and neural networks",
      "Identify ethical concerns and the need for responsible AI development"
    ]
  },
  {
    type: "screen",
    title: "AI Fundamentals",
    bullets: [
      "AI refers to computer systems that perform tasks requiring human intelligence",
      "AI uses algorithms and data to learn, make decisions, and improve over time",
      "It encompasses many techniques including machine learning and deep learning",
      "AI goals range from automating routine tasks to complex human interaction",
      "Applications span healthcare, finance, transportation, and education"
    ]
  },
  {
    type: "cyu",
    title: "Check Your Understanding",
    question: "What is the primary focus of Artificial Intelligence?",
    options: { A: "Creating intelligent machines that think like humans", B: "Developing algorithms for data analysis", C: "Designing computer networks", D: "Improving user experience" },
    correct: "A"
  },
  {
    type: "screen",
    title: "What is Artificial Intelligence?",
    bullets: [
      "AI is a branch of computer science focused on building intelligent systems",
      "Early AI systems were rule-based; modern AI uses machine learning",
      "Modern AI can improve over time without being explicitly reprogrammed",
      "Narrow AI is designed for specific tasks — all current AI is Narrow AI",
      "General AI, the ultimate goal, can perform any intellectual human task"
    ]
  },
  {
    type: "cyu",
    title: "Check Your Understanding",
    question: "What type of AI is currently used in most systems today?",
    options: { A: "Narrow AI", B: "General AI", C: "Superintelligence", D: "Artificial General Intelligence" },
    correct: "A"
  },
  {
    type: "screen",
    title: "Machine Learning Basics",
    bullets: [
      "Machine learning enables computers to learn from experience via algorithms",
      "Deep learning uses multi-layered neural networks to recognize complex patterns",
      "Popular frameworks include TensorFlow, PyTorch, and Scikit-learn",
      "Applications include recommendation systems, spam filters, and voice assistants",
      "Machine learning is a core subset powering most modern AI applications"
    ]
  },
  {
    type: "cyu",
    title: "Check Your Understanding",
    question: "What type of networks does deep learning use to recognize patterns?",
    options: { A: "Single-layered networks", B: "Multi-layered neural networks", C: "Rule-based systems", D: "Decision trees" },
    correct: "B"
  },
  {
    type: "summary",
    title: "Summary",
    content: "AI focuses on building systems that mimic human intelligence through machine learning and deep learning. All existing AI is Narrow AI — designed for specific tasks — though General AI remains the long-term goal. Ethical concerns including privacy, bias, and job displacement highlight the need for responsible development. Investing in education and ethical frameworks today will shape how safely we harness AI's power tomorrow."
  }
];

// ── Helper: fresh shadow object ──────────────────────────────────────────────
const makeShadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.18 });

// ── Slide builders ────────────────────────────────────────────────────────────

function buildTitleSlide(pres) {
  const slide = pres.addSlide();
  slide.background = { color: C.dark };

  // Large accent circle
  slide.addShape(pres.shapes.OVAL, {
    x: 7.2, y: -1.2, w: 5, h: 5,
    fill: { color: C.navy, transparency: 30 }, line: { color: C.navy, width: 0 }
  });

  // Tag
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5, y: 0.55, w: 2.2, h: 0.38,
    fill: { color: C.accent }, line: { color: C.accent, width: 0 }, rectRadius: 0.05
  });
  slide.addText("eLEARNING COURSE", {
    x: 0.5, y: 0.55, w: 2.2, h: 0.38,
    fontSize: 9, bold: true, color: C.white, align: "center", valign: "middle", margin: 0
  });

  slide.addText("Artificial Intelligence", {
    x: 0.5, y: 1.1, w: 9, h: 1.4,
    fontSize: 52, bold: true, color: C.white, fontFace: "Calibri"
  });
  slide.addText("An Overview", {
    x: 0.5, y: 2.45, w: 9, h: 0.7,
    fontSize: 26, color: C.ice, fontFace: "Calibri Light"
  });
  slide.addText("From fundamentals to ethics — a complete learning journey", {
    x: 0.5, y: 3.3, w: 7, h: 0.5,
    fontSize: 13, color: C.muted, italic: true
  });

  // Bottom bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 5.1, w: 10, h: 0.525,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 }
  });
  slide.addText("AI Learning Series  •  Module 1", {
    x: 0.5, y: 5.1, w: 9, h: 0.525,
    fontSize: 11, color: C.ice, valign: "middle"
  });
}

function buildIntroSlide(pres, screen) {
  const slide = pres.addSlide();
  slide.background = { color: C.white };

  // Left accent bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.12, h: 5.625,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 }
  });

  // Header band
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.12, y: 0, w: 9.88, h: 1.1,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 }
  });
  slide.addText("INTRODUCTION", {
    x: 0.4, y: 0, w: 9.4, h: 1.1,
    fontSize: 11, bold: true, color: C.ice, valign: "middle", charSpacing: 4
  });
  slide.addText(screen.title, {
    x: 0.4, y: 0.4, w: 9.4, h: 0.7,
    fontSize: 28, bold: true, color: C.white, valign: "middle"
  });

  // Content card
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 1.3, w: 9.3, h: 3.8,
    fill: { color: "F7F9FF" }, line: { color: C.ice, width: 1 }, shadow: makeShadow()
  });
  slide.addText(screen.content, {
    x: 0.7, y: 1.5, w: 8.7, h: 3.4,
    fontSize: 15, color: C.text, valign: "top", wrap: true, lineSpacingMultiple: 1.4
  });

  addFooter(slide, "Introduction");
}

function buildObjectivesSlide(pres, screen) {
  const slide = pres.addSlide();
  slide.background = { color: C.dark };

  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 1.2,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 }
  });
  slide.addText("LEARNING OBJECTIVES", {
    x: 0.5, y: 0, w: 9, h: 0.45,
    fontSize: 10, bold: true, color: C.ice, valign: "middle", charSpacing: 4
  });
  slide.addText(screen.title, {
    x: 0.5, y: 0.38, w: 9, h: 0.75,
    fontSize: 28, bold: true, color: C.white, valign: "middle"
  });

  const icons = ["01", "02", "03", "04", "05"];
  screen.objectives.forEach((obj, i) => {
    const y = 1.35 + i * 0.82;
    slide.addShape(pres.shapes.RECTANGLE, {
      x: 0.4, y, w: 9.2, h: 0.68,
      fill: { color: C.mid, transparency: 40 }, line: { color: C.accent, width: 1 }
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x: 0.4, y, w: 0.55, h: 0.68,
      fill: { color: C.accent }, line: { color: C.accent, width: 0 }
    });
    slide.addText(icons[i], {
      x: 0.4, y, w: 0.55, h: 0.68,
      fontSize: 13, bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });
    slide.addText(obj, {
      x: 1.1, y: y + 0.04, w: 8.3, h: 0.6,
      fontSize: 13.5, color: C.ice, valign: "middle"
    });
  });

  addFooter(slide, "Objectives", true);
}

function buildScreenSlide(pres, screen, index) {
  const slide = pres.addSlide();
  slide.background = { color: C.white };

  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 1.15,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 }
  });
  slide.addText(`SCREEN ${index}`, {
    x: 0.5, y: 0, w: 9, h: 0.42,
    fontSize: 10, bold: true, color: C.ice, valign: "middle", charSpacing: 4
  });
  slide.addText(screen.title, {
    x: 0.5, y: 0.35, w: 9, h: 0.75,
    fontSize: 26, bold: true, color: C.white, valign: "middle"
  });

  const items = screen.bullets.map((b, i) => ([
    { text: `${i + 1}`, options: { color: C.accent, bold: true, fontSize: 13 } },
    { text: `  ${b}`, options: { color: C.text, fontSize: 13.5, breakLine: i < screen.bullets.length - 1 } }
  ])).flat();

  slide.addText(items, {
    x: 0.5, y: 1.3, w: 9, h: 4.0,
    valign: "top", paraSpaceAfter: 14, wrap: true
  });

  addFooter(slide, screen.title);
}

function buildCYUSlide(pres, screen) {
  const slide = pres.addSlide();
  slide.background = { color: C.dark };

  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 1.1,
    fill: { color: C.orange }, line: { color: C.orange, width: 0 }
  });
  slide.addText("CHECK YOUR UNDERSTANDING", {
    x: 0.5, y: 0, w: 9, h: 0.42,
    fontSize: 10, bold: true, color: C.white, valign: "middle", charSpacing: 4
  });
  slide.addText("Quiz", {
    x: 0.5, y: 0.35, w: 9, h: 0.7,
    fontSize: 26, bold: true, color: C.white, valign: "middle"
  });

  // Question card
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 1.2, w: 9.2, h: 0.9,
    fill: { color: C.mid }, line: { color: C.accent, width: 1 }, shadow: makeShadow()
  });
  slide.addText(`Q:  ${screen.question}`, {
    x: 0.6, y: 1.25, w: 8.8, h: 0.8,
    fontSize: 14.5, bold: true, color: C.white, valign: "middle", wrap: true
  });

  const optColors = { A: "2ECC71", B: "3498DB", C: "9B59B6", D: "E74C3C" };
  Object.entries(screen.options).forEach(([key, val], i) => {
    const x = i % 2 === 0 ? 0.4 : 5.2;
    const y = i < 2 ? 2.3 : 3.35;
    const isCorrect = key === screen.correct;
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y, w: 4.5, h: 0.78,
      fill: { color: isCorrect ? optColors[key] : C.mid },
      line: { color: optColors[key], width: isCorrect ? 0 : 1 },
      shadow: makeShadow()
    });
    slide.addText(`${key})  ${val}${isCorrect ? "  ✓" : ""}`, {
      x: x + 0.15, y: y + 0.05, w: 4.2, h: 0.68,
      fontSize: 13, color: C.white, valign: "middle", bold: isCorrect, wrap: true
    });
  });

  slide.addText(`Correct Answer: ${screen.correct}`, {
    x: 0.4, y: 4.35, w: 9.2, h: 0.45,
    fontSize: 12, color: C.green, bold: true, italic: true
  });

  addFooter(slide, "Quiz", true);
}

function buildSummarySlide(pres, screen) {
  const slide = pres.addSlide();
  slide.background = { color: C.dark };

  slide.addShape(pres.shapes.OVAL, {
    x: 6.5, y: -1, w: 5, h: 5,
    fill: { color: C.navy, transparency: 40 }, line: { color: C.navy, width: 0 }
  });

  slide.addText("SUMMARY", {
    x: 0.5, y: 0.4, w: 8, h: 0.4,
    fontSize: 10, bold: true, color: C.ice, charSpacing: 4
  });
  slide.addText(screen.title, {
    x: 0.5, y: 0.75, w: 8, h: 0.9,
    fontSize: 36, bold: true, color: C.white, fontFace: "Calibri"
  });

  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 1.8, w: 9.2, h: 3.2,
    fill: { color: C.mid, transparency: 30 }, line: { color: C.accent, width: 1 }, shadow: makeShadow()
  });
  slide.addText(screen.content, {
    x: 0.7, y: 1.95, w: 8.7, h: 2.9,
    fontSize: 14.5, color: C.ice, valign: "top", wrap: true, lineSpacingMultiple: 1.5
  });

  addFooter(slide, "Summary", true);
}

function addFooter(slide, label, light = false) {
  const fg = light ? C.muted : C.muted;
  slide.addText(`AI Learning Series  •  ${label}`, {
    x: 0.4, y: 5.3, w: 9.2, h: 0.3,
    fontSize: 9, color: fg, italic: true
  });
}

// ── Main ──────────────────────────────────────────────────────────────────────
async function buildPresentation() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.title = "Artificial Intelligence: An Overview";
  pres.author = "AI Learning Series";

  buildTitleSlide(pres);

  let screenIndex = 1;
  for (const screen of storyboard) {
    if (screen.type === "introduction") buildIntroSlide(pres, screen);
    else if (screen.type === "objectives") buildObjectivesSlide(pres, screen);
    else if (screen.type === "screen") { buildScreenSlide(pres, screen, screenIndex); screenIndex++; }
    else if (screen.type === "cyu") buildCYUSlide(pres, screen);
    else if (screen.type === "summary") buildSummarySlide(pres, screen);
  }

  await pres.writeFile({ fileName: "storyboard_pro.pptx" });
  console.log("✅ storyboard_pro.pptx saved!");
}

buildPresentation().catch(console.error);
