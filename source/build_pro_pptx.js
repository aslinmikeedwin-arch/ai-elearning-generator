const pptxgen = require("pptxgenjs");
const fs = require("fs");

const C = {
  navy:   "1E2761",
  mid:    "2E3F8F",
  dark:   "0F1640",
  ice:    "CADCFC",
  white:  "FFFFFF",
  accent: "5B8CFF",
  green:  "2ECC71",
  orange: "E67E22",
  muted:  "8892B0",
};

const TYPE_BG = {
  introduction: "1E2761",
  objectives:   "2E3F8F",
  screen:       "1A6B3C",
  cyu:          "B85A00",
  summary:      "6B2FA0",
};

const TYPE_LABELS = {
  introduction: "INTRODUCTION",
  objectives:   "OBJECTIVES",
  screen:       "CONTENT SCREEN",
  cyu:          "CHECK YOUR UNDERSTANDING",
  summary:      "SUMMARY",
};

const shadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.18 });

function addTitleSlide(pres, topic) {
  const slide = pres.addSlide();
  slide.background = { color: C.dark };
  slide.addShape(pres.shapes.OVAL, { x: 7.2, y: -1.2, w: 5, h: 5, fill: { color: C.navy, transparency: 30 }, line: { color: C.navy, width: 0 } });
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 0.55, w: 2.4, h: 0.38, fill: { color: C.accent }, line: { color: C.accent, width: 0 }, rectRadius: 0.05 });
  slide.addText("eLEARNING COURSE", { x: 0.5, y: 0.55, w: 2.4, h: 0.38, fontSize: 9, bold: true, color: C.white, align: "center", valign: "middle", margin: 0 });
  slide.addText(topic, { x: 0.5, y: 1.1, w: 9, h: 1.4, fontSize: 44, bold: true, color: C.white, fontFace: "Calibri" });
  slide.addText("AI-Generated eLearning Storyboard", { x: 0.5, y: 2.45, w: 9, h: 0.7, fontSize: 22, color: C.ice, fontFace: "Calibri Light" });
  slide.addText("Automatically generated using local AI — Mediant Labs 2026", { x: 0.5, y: 3.3, w: 7, h: 0.5, fontSize: 12, color: C.muted, italic: true });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.1, w: 10, h: 0.525, fill: { color: C.navy }, line: { color: C.navy, width: 0 } });
  slide.addText(`${topic}  •  eLearning Series`, { x: 0.5, y: 5.1, w: 9, h: 0.525, fontSize: 11, color: C.ice, valign: "middle" });
}

function addContentSlide(pres, screen, topic) {
  const stype = screen.type;
  const bg = TYPE_BG[stype] || C.navy;
  const label = TYPE_LABELS[stype] || stype.toUpperCase();
  const slide = pres.addSlide();
  slide.background = { color: C.dark };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 1.2, fill: { color: bg }, line: { color: bg, width: 0 } });
  slide.addText(label, { x: 0.4, y: 0, w: 9, h: 0.45, fontSize: 10, bold: true, color: C.ice, valign: "middle", charSpacing: 3 });
  slide.addText(screen.title || label, { x: 0.4, y: 0.38, w: 9, h: 0.75, fontSize: 26, bold: true, color: C.white, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: 1.35, w: 9.2, h: 3.9, fill: { color: C.mid, transparency: 35 }, line: { color: C.accent, width: 1 }, shadow: shadow() });
  let content = "";
  if (stype === "cyu") {
    content = `Q: ${screen.question || ""}\n\n`;
    const opts = screen.options || {};
    for (const [k, v] of Object.entries(opts)) {
      const tick = k === screen.correct_answer ? "  ✓" : "";
      content += `${k})  ${v}${tick}\n`;
    }
    content += `\nCorrect Answer: ${screen.correct_answer || ""}`;
  } else {
    content = (screen.content || "").replace(/^Title:.*\n?/im, "").trim();
  }
  slide.addText(content, { x: 0.6, y: 1.5, w: 8.8, h: 3.6, fontSize: 14, color: C.ice, valign: "top", wrap: true, lineSpacingMultiple: 1.4 });
  slide.addText(`${topic}  •  ${label}`, { x: 0.4, y: 5.3, w: 9.2, h: 0.3, fontSize: 9, color: C.muted, italic: true });
}

async function buildPro(jsonFile, outputFile, topic) {
  const storyboard = JSON.parse(fs.readFileSync(jsonFile, "utf8"));
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.title = topic;
  addTitleSlide(pres, topic);
  for (const screen of storyboard) {
    addContentSlide(pres, screen, topic);
  }
  await pres.writeFile({ fileName: outputFile });
  console.log(`✅ Saved: ${outputFile}`);
}

const args = process.argv.slice(2);
buildPro(args[0], args[1], args[2] || "eLearning Course").catch(console.error);
