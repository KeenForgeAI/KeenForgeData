# KeenForgeData

**高质量小众视觉数据集 —— 重新标注 · 清理 · 完整文档化 · 双渠道开源**
**High-quality niche vision datasets — re-annotated, cleaned, documented, and published openly.**

[English](#english) · [中文](#中文)

---

## English

### What is this repository?

`KeenForgeData` is the **dataset index** of **[KeenForgeAI](https://huggingface.co/KeenForgeAI)**.

The datasets themselves live on **Hugging Face** and **ModelScope** — this repository is the one
place that records *what* we publish, *why*, and *how* each release was corrected. Each dataset
ships with full provenance, a correction report, licensing information and citations inside its
own repository.

Everything here is produced with **[KeenForge](https://github.com/KeenForgeAI/KeenForge)** — a
local-first, open-source annotation & training desktop tool (100% offline, MIT licensed).

### 📦 Published datasets

<!-- GEN:TABLE -->
| Dataset | Domain | Images | Boxes | Hugging Face | ModelScope |
|---|---|---|---|---|---|
| **PKU-Market-PCB-corrected** | 🔧 Industrial — PCB | 693 | 2,953 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/PKU-Market-PCB-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PKU-Market-PCB-corrected) |
| **DeepPCB-corrected** | 🔌 Industrial — PCB | 1,499 | 10,004 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/DeepPCB-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/DeepPCB-corrected) |
| **NEU-DET-corrected** | 🔩 Industrial — steel surface | 1,797 | 4,177 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/NEU-DET-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/NEU-DET-corrected) |
| **GC10-DET-corrected** | 🏭 Industrial — steel surface | 2,280 | 3,542 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/GC10-DET-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/GC10-DET-corrected) |
| **TXL-PBC-corrected** | 🩸 Medical — hematology | 1,256 | 18,098 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/TXL-PBC-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/TXL-PBC-corrected) |
| **raccoon-corrected** | 🦝 Wildlife | 193 | 211 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/raccoon-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/raccoon-corrected) |
<!-- GEN:TABLE_END -->

### 🔗 All links

| | |
|---|---|
| **All datasets on Hugging Face** | <https://huggingface.co/KeenForgeAI> |
| **All datasets on ModelScope** | <https://www.modelscope.ai/organizations/KeenForgeAI> |
| **The annotation tool (KeenForge)** | <https://github.com/KeenForgeAI/KeenForge> |
| **Organization website** | <https://keenforgeai.github.io/> |
| **Issues / requests** | <https://github.com/KeenForgeAI/KeenForge/issues> |

Direct dataset links:

<!-- GEN:LINKS -->
- **PKU-Market-PCB-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/PKU-Market-PCB-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PKU-Market-PCB-corrected)
- **DeepPCB-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/DeepPCB-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/DeepPCB-corrected)
- **NEU-DET-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/NEU-DET-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/NEU-DET-corrected) · [DOI](https://doi.org/10.57967/hf/10536)
- **GC10-DET-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/GC10-DET-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/GC10-DET-corrected) · [DOI](https://doi.org/10.57967/hf/10526)
- **TXL-PBC-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/TXL-PBC-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/TXL-PBC-corrected) · [DOI](https://doi.org/10.57967/hf/10527)
- **raccoon-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/raccoon-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/raccoon-corrected) · [DOI](https://doi.org/10.57967/hf/10528)
<!-- GEN:LINKS_END -->

### 🧹 What "corrected" means

Most public datasets are large but noisy — loose boxes, missed objects, mislabels, duplicates.
We take public *niche* datasets and:

1. **Re-annotate** them with a human-in-the-loop workflow in KeenForge
   (AI pre-labels → every image reviewed by a human → independent cross-check).
2. **Clean** them — tighten boxes, fix mislabels, add missed instances, remove duplicates and
   un-annotated images.
3. **Document** them — full provenance, source datasets, a correction report and citations.
4. **Publish** them openly on Hugging Face **and** ModelScope.

Every release is a **structural clean-up of the original annotations**, not a from-scratch
re-annotation, unless its own README says otherwise. Image pixels are never modified.

### 📚 Dataset details

<!-- GEN:DETAILS -->
#### 🔧 PKU-Market-PCB-corrected — 693 images · 2,953 boxes

PCB defect detection, 6 classes, COCO + Pascal VOC + YOLO annotations, board-disjoint split. Cleaned version of **PKU-Market-PCB** (Huang & Wei, [arXiv:1901.08204](https://arxiv.org/abs/1901.08204), 2019): a stray `data.yaml` was removed; Pascal VOC and YOLO annotations were added; and a **board-disjoint split** (541 / 152) was added because the upstream split places all 10 base boards in both halves (100 % board-level leakage — a model evaluated on it sees boards it has memorized). No bounding box was modified. Upstream licence unstated.

#### 🔌 DeepPCB-corrected — 1,499 images · 10,004 boxes

PCB defect detection, 6 classes, with defect-free template pairs. TXT + Pascal VOC + YOLO annotations. Cleaned version of **DeepPCB** (Tang et al., [arXiv:1902.06197](https://arxiv.org/abs/1902.06197)): the upstream split lists referenced files that do not exist (all 1,500 image paths broken) and are rewritten here; 1 image with annotations burned into its pixels and 1 orphan template were removed; 61 RGB-mode images were normalised to grayscale (content unchanged); Pascal VOC and YOLO annotations added. MIT licensed.

#### 🔩 NEU-DET-corrected — 1,797 images · 4,177 boxes

DOI: [10.57967/hf/10536](https://doi.org/10.57967/hf/10536)

Hot-rolled steel strip surface defects, 6 classes, Pascal VOC + YOLO annotations. Cleaned version of the **NEU Surface Defect Database (NEU-DET)** (He et al., *IEEE TIM* 69(4):1493-1504, 2020, [doi:10.1109/TIM.2019.2915404](https://doi.org/10.1109/TIM.2019.2915404)): 3 duplicate images (1 exact, 2 near-duplicates under rotation / shift) and 3 duplicate boxes removed, a reproducible 80/10/10 split added, and the data re-packaged in both Pascal VOC and YOLO format. Structural clean-up only — no re-annotation.

#### 🏭 GC10-DET-corrected — 2,280 images · 3,542 boxes

DOI: [10.57967/hf/10526](https://doi.org/10.57967/hf/10526)

Hot-rolled steel strip surface defects, 10 classes, Pascal VOC annotations. Cleaned version of [GC10-DET](https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets): 13 duplicate images removed, 26 un-annotated images removed, and 132 annotation files with wrong class names fixed (`10_yaozhed` → `10_yaozhe`, one garbage label `d` → `1_chongkong`).

#### 🩸 TXL-PBC-corrected — 1,256 images · 18,098 boxes

DOI: [10.57967/hf/10527](https://doi.org/10.57967/hf/10527)

Peripheral blood cell detection (WBC / RBC / Platelets), 3 classes, YOLO format. Corrected version of the **TXL-PBC** dataset (Gan, Li & Wang, *Scientific Data* 12:1694, 2025, [doi:10.1038/s41597-025-05980-z](https://doi.org/10.1038/s41597-025-05980-z)): 4 duplicate images removed, labels and README corrected.

#### 🦝 raccoon-corrected — 193 images · 211 boxes

DOI: [10.57967/hf/10528](https://doi.org/10.57967/hf/10528)

The classic Raccoon detection dataset, fully re-annotated. Boxes tightened (average IoU 0.810 against the original), mislabels fixed, 7 duplicate images removed, missed instances added.
<!-- GEN:DETAILS_END -->

### ⚖️ License & attribution

**Each dataset keeps its own upstream license and attribution** — see the `LICENSE` and
`README.md` inside the corresponding Hugging Face / ModelScope repository. Our modifications
(cleaning, de-duplication, corrections, documentation) are released openly.

> ⚠️ **Note on GC10-DET:** the original authors have never stated a license for their dataset
> (their repository has no LICENSE file and the question remains unanswered upstream). The
> upstream copyright status is therefore undetermined — verify it before commercial use.
> See the `LICENSE` file in the GC10-DET-corrected repository for details.

### 🤝 Contributing

- **Found a problem** in one of our datasets? Please open an
  [issue](https://github.com/KeenForgeAI/KeenForge/issues) — corrections are very welcome.
- **Re-annotated a niche dataset** with KeenForge and want to publish it? Open an issue and we
  will help you clean, document and release it.
- **Want to help build the tool?** KeenForge is MIT-licensed; PRs, docs and translations are all
  welcome at <https://github.com/KeenForgeAI/KeenForge>.

---

## 中文

### 这个仓库是什么？

`KeenForgeData` 是 **[KeenForgeAI](https://huggingface.co/KeenForgeAI)** 的**数据集索引仓库**。

数据集本身托管在 **Hugging Face** 和 **ModelScope** 上；本仓库是统一记录「我们发布了什么、
为什么发布、每一版修正了什么」的地方。每个数据集都自带完整的来源说明、修正报告、许可证信息
和引用信息。

所有数据都由 **[KeenForge](https://github.com/KeenForgeAI/KeenForge)** 生产 —— 一款本地优先的
开源标注与训练桌面工具（100% 离线，MIT 许可）。

### 📦 已发布数据集

| 数据集 | 领域 | 图片 | 标注框 | Hugging Face | ModelScope |
|---|---|---|---|---|---|
| **GC10-DET-corrected** | 🏭 工业 — 钢板表面 | 2,280 | 3,542 | [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/GC10-DET-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/GC10-DET-corrected) |
| **TXL-PBC-corrected** | 🩸 医疗 — 血液学 | 1,256 | 18,098 | [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/TXL-PBC-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/TXL-PBC-corrected) |
| **raccoon-corrected** | 🦝 野生动物 | 193 | 211 | [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/raccoon-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/raccoon-corrected) |

### 🔗 总链接

| | |
|---|---|
| **Hugging Face 全部数据集** | <https://huggingface.co/KeenForgeAI> |
| **ModelScope 全部数据集** | <https://www.modelscope.ai/organizations/KeenForgeAI> |
| **标注工具 KeenForge** | <https://github.com/KeenForgeAI/KeenForge> |
| **组织官网** | <https://keenforgeai.github.io/> |
| **问题反馈** | <https://github.com/KeenForgeAI/KeenForge/issues> |

### 🧹 「修正版」意味着什么

公开数据集往往「大而糙」—— 框松、漏标、错标、重复。我们把公开的**小众数据集**重新整理：

1. **重新精标**：用 KeenForge 的人机协同流程（AI 预标注 → 逐张人工复核 → 交叉复核）
2. **清理**：收紧框、改错标、补漏标、删除重复图片与无标注图片
3. **完整文档化**：来源、修正报告、引用信息齐全
4. **双渠道开源发布**：Hugging Face 与 ModelScope

每一版都是对**原有标注的结构性清理**，而不是从零重标（除非该数据集自己的 README 另有说明）。
**图片像素从不修改。**

### 📚 各数据集简介

- **🏭 GC10-DET-corrected**（2,280 张 / 3,542 框）：热轧带钢表面缺陷，10 类，Pascal VOC 格式。
  修正了 13 张重复图片、26 张无标注图片，以及 132 个类别名错误的标注文件
  （`10_yaozhed` → `10_yaozhe`，垃圾标签 `d` → `1_chongkong`）。
- **🩸 TXL-PBC-corrected**（1,256 张 / 18,098 框）：外周血细胞检测（白细胞 / 红细胞 / 血小板），
  3 类，YOLO 格式。修正了 4 张重复图片，并订正了标签与说明文档。
- **🦝 raccoon-corrected**（193 张 / 211 框）：经典浣熊检测数据集的完全重标版 ——
  框全部收紧（对原标注平均 IoU 0.810）、修正错标、删除 7 张重复图片、补上漏标目标。

### ⚖️ 许可证与署名

**每个数据集保留其自身的上游许可证与署名**，详见对应 Hugging Face / ModelScope 仓库内的
`LICENSE` 与 `README.md`。我们对数据集的修改部分（清理、去重、修正、文档）开源发布。

> ⚠️ **关于 GC10-DET**：原始作者**从未声明**该数据集的许可证（其仓库没有 LICENSE 文件，
> 上游 issue 至今无人回复），因此上游版权状态未定 —— **商用前请自行确认**。
> 详见 GC10-DET-corrected 仓库内的 `LICENSE` 文件。

### 🤝 参与共建

- **发现数据问题**？欢迎在 [issue](https://github.com/KeenForgeAI/KeenForge/issues) 里反馈，修正非常欢迎。
- **用小众数据集做了重新标注**，想发布出来？开个 issue，我们帮你清理、文档化并发布。
- **想一起做工具**？KeenForge 是 MIT 许可，欢迎 PR、文档和翻译。

---

<p align="center">
  <b>Only high-quality data can push visual AI forward.</b><br>
  <b>只有高质量的数据集，才能推动视觉 AI 的发展。</b>
</p>
