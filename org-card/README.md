---
title: KeenForgeAI
emoji: 🔥
colorFrom: indigo
colorTo: purple
sdk: static
pinned: false
---

# 🔥 KeenForgeAI

**Forging high-quality, niche vision datasets — and the open-source tool to build them.**

KeenForgeAI is an open-source organization focused on **re-annotating and curating small, high-quality
niche datasets** for computer vision, and on building **[KeenForge](https://github.com/KeenForgeAI/KeenForge)** —
a local-first annotation & training desktop tool that makes this kind of careful work practical.

🔗 **GitHub:** <https://github.com/KeenForgeAI/KeenForge> · **Datasets:** <https://huggingface.co/KeenForgeAI>

---

## 🛠 The tool: KeenForge

> **CVPR 2026 Demo Track** · Formerly *AutoLabel Pro*

KeenForge is a desktop application that lets you train your own object-detection model
**without writing a single line of code**. Import images, draw a few boxes, and the AI trains
itself in the background. **Your data never leaves your computer.**

| | KeenForge |
|---|---|
| **Deployment** | Double-click an `.exe` (Windows) |
| **Privacy** | **100% local & offline** — images are never uploaded |
| **AI assistance** | Built-in **YOLO-World zero-shot** detection |
| **Auto-training** | Triggers automatically after ~15 labels |
| **Model ownership** | **You own your model** |
| **Price** | **Free & open source (MIT)** |

**Core features**

- **Zero-shot cold start** — type any object name (`"welding defect"`, `"safety helmet"`, `"platelet"`)
  and KeenForge finds it immediately. No pre-training required.
- **Self-looping active learning** — label ~15 images → auto-train in the background → the model
  suggests better boxes on the next images → repeat. The more you label, the smarter it gets.
- **Infinite canvas** — smooth pan / zoom for large, high-resolution images.
- **Export anywhere** — YOLO / COCO / VOC formats.

🎬 [Watch the demo](https://www.youtube.com/watch?v=shU62O8_40E) · ⭐ [Star on GitHub](https://github.com/KeenForgeAI/KeenForge)

---

## 🎯 Our mission: high-quality niche datasets

Most public datasets are large but noisy. Smaller **well-annotated** datasets in *niche domains*
are often the ones that actually move research forward — yet they are the hardest to find.

We take public niche datasets — **industrial / manufacturing**, **medical & microscopy**,
**agriculture**, **safety**, and more — and:

1. **Re-annotate them carefully** with a human-in-the-loop workflow in KeenForge
   (AI pre-labels → every image reviewed by a human → independent cross-check by a second annotator).
2. **Clean them** — tighten boxes, fix mislabels, add missed instances, remove duplicates.
3. **Document them** — full provenance, source datasets, correction reports and citations.
4. **Publish them openly** on **Hugging Face** and **ModelScope**.

### Published datasets

<!-- GEN:CARD_TABLE -->
| Dataset | Domain | Size | Description |
|---|---|---|---|
| [`GC10-DET-corrected`](https://huggingface.co/datasets/KeenForgeAI/GC10-DET-corrected) | 🏭 Industrial (steel) | 2,280 images · 3,542 boxes | Hot-rolled steel strip surface defects, 10 classes (Pascal VOC) — cleaned version of GC10-DET |
| [`TXL-PBC-corrected`](https://huggingface.co/datasets/KeenForgeAI/TXL-PBC-corrected) | 🩸 Medical (hematology) | 1,256 images · 18,098 boxes | Peripheral blood cell detection (WBC / RBC / Platelets) — corrected version of TXL-PBC |
| [`raccoon-corrected`](https://huggingface.co/datasets/KeenForgeAI/raccoon-corrected) | 🦝 Wildlife | 193 images · 211 boxes | Fully re-annotated version of the classic Raccoon detection dataset |
<!-- GEN:CARD_TABLE_END -->

*More coming — PCB, agriculture, safety, …*

---

## 💡 What we believe

> **Only high-quality data can push visual AI forward.**

Architectures are converging and compute keeps getting cheaper — but a model is only ever as good
as the labels it learns from. We optimise for annotation quality, provenance and reproducibility,
not raw size.

---

## 🤝 Join us

KeenForgeAI is a community effort. You can help by:

- **Use KeenForge** — report bugs or request features in the [issue tracker](https://github.com/KeenForgeAI/KeenForge/issues).
- **Contribute code** — MIT-licensed; PRs, docs and translations welcome.
- **Contribute datasets** — re-annotated a niche dataset? Open an issue and we'll help you publish it.
- **Spread the word** — star the repo and share your workflow.

The best vision datasets will come from many small communities working carefully, not from a few
giant scrapes. **Come build with us.**

---

## 中文版

**KeenForgeAI 是一个开源组织，专注于「高质量小众视觉数据集」的重新标注与整理，并开发配套的本地化标注训练工具 [KeenForge](https://github.com/KeenForgeAI/KeenForge)。**

### 🛠 工具：KeenForge

> **CVPR 2026 Demo Track** · 前身为 *AutoLabel Pro*

KeenForge 是一款桌面应用，**无需写一行代码**就能训练你自己的目标检测模型：导入图片 → 画几个框 →
AI 在后台自动训练。**数据全程不离开你的电脑。**

- **零样本冷启动**：直接输入要检测的目标名称（如「焊接缺陷」「安全帽」「血小板」），
  内置 YOLO-World 立即识别，无需预训练
- **自循环主动学习**：标注约 15 张图 → 后台自动训练 → 模型在新图上给出更好的框 → 继续标注，越标越准
- **无限画布**：大图 / 高分辨率图片流畅缩放平移
- **一键导出**：YOLO / COCO / VOC 格式
- **100% 本地离线** · **模型归你所有** · **完全免费开源（MIT）**

🎬 [演示视频](https://www.youtube.com/watch?v=shU62O8_40E) ｜ ⭐ [GitHub 仓库](https://github.com/KeenForgeAI/KeenForge)

### 🎯 我们的使命

公开数据集往往「大而糙」——框松、漏标、错标、重复。真正推动研究的，常常是那些**小众领域里标注精良**
的小数据集，但它们恰恰最难找。

我们把公开的小众数据集（**工业制造**、**医疗显微**、**农业**、**安防**等）重新整理：

1. 用 KeenForge 的人机协同流程**重新精标**（AI 预标注 → 逐张人工复核 → 第二人交叉复核）
2. **清理**：收紧框、改错标、补漏标、去重复
3. **完整文档化**：来源、修正报告、引用信息齐全
4. **开源发布**到 **Hugging Face** 与 **ModelScope**

<!-- GEN:CARD_ZH -->
**已发布数据集**：🏭 [`GC10-DET-corrected`](https://huggingface.co/datasets/KeenForgeAI/GC10-DET-corrected)（工业 — 钢板表面，2,280 张 / 3,542 框）、🩸 [`TXL-PBC-corrected`](https://huggingface.co/datasets/KeenForgeAI/TXL-PBC-corrected)（医疗 — 血液学，1,256 张 / 18,098 框）、🦝 [`raccoon-corrected`](https://huggingface.co/datasets/KeenForgeAI/raccoon-corrected)（野生动物，193 张 / 211 框）
<!-- GEN:CARD_ZH_END -->

### 💡 我们的理念

> **只有高质量的数据集，才能推动视觉 AI 的发展。**

模型架构在趋同、算力越来越便宜，但模型的上限永远由标注质量决定。我们死磕的是标注质量、
可溯源性和可复现性，而不是数据量。

### 🤝 加入我们

- **用 KeenForge**——提 issue / 提需求
- **贡献代码**（MIT 许可，欢迎 PR、文档、翻译）
- **贡献数据集**——用 KeenForge 重新标注了小众数据集？开个 issue，我们帮你发布
- **帮忙传播**——给仓库点个 star，分享你的工作流

我们相信，未来最好的视觉数据集会来自许多小社区认真细致的工作，而不是少数几个巨大的爬取。
**欢迎一起共建 KeenForgeAI。**

🔗 GitHub: <https://github.com/KeenForgeAI/KeenForge> ｜ Hugging Face: <https://huggingface.co/KeenForgeAI>
