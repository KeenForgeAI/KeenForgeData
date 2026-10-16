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
| **KIT_BallScrew_Defects-corrected** | 🔩 Industrial — ball-screw surface inspection | 21,835 | 0 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/KIT_BallScrew_Defects-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/KIT_BallScrew_Defects-corrected) |
| **TrafficSigns_YOLO-corrected** | 🚦 Transport — traffic sign detection | 6,000 | 6,000 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/TrafficSigns_YOLO-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/TrafficSigns_YOLO-corrected) |
| **RoadCrack_DL_HY-corrected** | 🛣️ Civil — pavement crack detection | 2,189 | 2,677 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/RoadCrack_DL_HY-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/RoadCrack_DL_HY-corrected) |
| **VisuCeram_500x500-corrected** | 🧱 Industrial — ceramic surface inspection | 3,264 | 6,042 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/VisuCeram_500x500-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/VisuCeram_500x500-corrected) |
| **PV_Multi_Defect-corrected** | ☀️ Energy — photovoltaic inspection | 1,044 | 3,403 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/PV_Multi_Defect-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PV_Multi_Defect-corrected) |
| **DBA_Fire_Smoke-corrected** | 🔥 Safety — fire & smoke detection | 3,846 | 7,988 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/DBA_Fire_Smoke-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/DBA_Fire_Smoke-corrected) |
| **CPLID_Insulators-corrected** | ⚡ Energy — power-line inspection | 845 | 1,566 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/CPLID_Insulators-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/CPLID_Insulators-corrected) |
| **PlantDoc-corrected** | 🌱 Agriculture — plant disease | 2,565 | 8,887 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/PlantDoc-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PlantDoc-corrected) |
| **PCB_AoI_KubeEdge-corrected** | 🖥️ Industrial — PCB | 233 | 1,011 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/PCB_AoI_KubeEdge-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PCB_AoI_KubeEdge-corrected) |
| **MagneticTile-corrected** | 🧲 Industrial — magnetic tile | 1,318 | 437 | [![HF](https://img.shields.io/badge/HF-dataset-yellow)](https://huggingface.co/datasets/KeenForgeAI/MagneticTile-corrected) | [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/MagneticTile-corrected) |
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
- **KIT_BallScrew_Defects-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/KIT_BallScrew_Defects-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/KIT_BallScrew_Defects-corrected) · [DOI](https://doi.org/10.57967/hf/11010)
- **TrafficSigns_YOLO-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/TrafficSigns_YOLO-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/TrafficSigns_YOLO-corrected) · [DOI](https://doi.org/10.57967/hf/10898)
- **RoadCrack_DL_HY-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/RoadCrack_DL_HY-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/RoadCrack_DL_HY-corrected) · [DOI](https://doi.org/10.57967/hf/10896)
- **VisuCeram_500x500-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/VisuCeram_500x500-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/VisuCeram_500x500-corrected) · [DOI](https://doi.org/10.57967/hf/10884)
- **PV_Multi_Defect-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/PV_Multi_Defect-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PV_Multi_Defect-corrected) · [DOI](https://doi.org/10.57967/hf/10882)
- **DBA_Fire_Smoke-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/DBA_Fire_Smoke-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/DBA_Fire_Smoke-corrected) · [DOI](https://doi.org/10.57967/hf/10880)
- **CPLID_Insulators-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/CPLID_Insulators-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/CPLID_Insulators-corrected) · [DOI](https://doi.org/10.57967/hf/10878)
- **PlantDoc-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/PlantDoc-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PlantDoc-corrected) · [DOI](https://doi.org/10.57967/hf/10678)
- **PCB_AoI_KubeEdge-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/PCB_AoI_KubeEdge-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PCB_AoI_KubeEdge-corrected) · [DOI](https://doi.org/10.57967/hf/10677)
- **MagneticTile-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/MagneticTile-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/MagneticTile-corrected) · [DOI](https://doi.org/10.57967/hf/10659)
- **PKU-Market-PCB-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/PKU-Market-PCB-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/PKU-Market-PCB-corrected) · [DOI](https://doi.org/10.57967/hf/10554)
- **DeepPCB-corrected** — [Hugging Face](https://huggingface.co/datasets/KeenForgeAI/DeepPCB-corrected) · [ModelScope](https://www.modelscope.ai/datasets/KeenForgeAI/DeepPCB-corrected) · [DOI](https://doi.org/10.57967/hf/10551)
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
#### 🔩 KIT_BallScrew_Defects-corrected — 21,835 images · 0 boxes

DOI: [10.57967/hf/11010](https://doi.org/10.57967/hf/11010)

Ball-screw surface defect image classification (pitting / contaminated / normal), 3 classes, ImageFolder layout, labels re-indexed 3/6/8→0/1/2. First classification dataset in the collection. Cleaned, re-indexed, split and standardized **image-classification** version of the **Tri-classified Ball Screw Surface Defects dataset (KIT-BS-recls)** (Xue, Zhang, Xie, Puchta & Fleischer, *Neurocomputing* 2025, DOI 10.1016/j.neucom.2025.131291; upstream [fenghsueh/Triclass-BSDefects](https://github.com/fenghsueh/Triclass-BSDefects); licensed **CC BY-SA 4.0**): the archive was converted to a folder-based classification layout (`images/<split>/<class>/`); the upstream labels, which were the **non-contiguous ids 3 / 6 / 8** (pitting / contaminated / normal), were **remapped to 0 / 1 / 2**; a seeded, class-stratified **70 / 15 / 15** split was added (upstream has none): **15,288 / 3,276 / 3,271**; near-identical images (identical 8×8-dHash and 32×32 pixel-MSE ≤ 1) were kept on one side of the split; filenames containing parentheses (`P(123).png`) were normalised; and `classes.txt`, `data.yaml` and `labels.csv` were generated. **All 21,835 images are byte-for-byte identical** to upstream. 3 classes: `pitting` (10,760), `contaminated` (7,523), `normal` (3,552). Task: image classification (one label per image, no bounding boxes).

#### 🚦 TrafficSigns_YOLO-corrected — 6,000 images · 6,000 boxes

DOI: [10.57967/hf/10898](https://doi.org/10.57967/hf/10898)

Traffic sign detection (left/straight/right/dead-end/no-entry/stop), 6 classes, Pascal VOC + YOLO annotations, with a leak-safe split that keeps near-identical augmentations on one side. Leak-safe, standardized version of the **Traffic Signs Dataset** for YOLOv8–YOLOv11 benchmarking (Reveles-Martínez, Gamboa-Rosales et al., *Technologies* 2025; upstream [rrevelesm/Articulos-Benchmarking-YOLOv8-to-YOLOv11](https://github.com/rrevelesm/Articulos-Benchmarking-YOLOv8-to-YOLOv11); upstream licence unstated): the 6,000 images are heavily Roboflow-augmented, and **2,526 of them form near-identical clusters** (identical 8×8-dHash and 32×32 pixel-MSE ≤ 1; largest cluster 25 images); the upstream random split scattered these near-identical copies across train/valid/test (leakage). Each near-identical cluster is now assigned **entirely to one side** of a seeded, class-stratified split (**4259 / 858 / 883**) that replaces the upstream **4200 / 1200 / 600**; Pascal VOC XML annotations, `classes.txt`, `data.yaml` and per-split CSVs were added. **All 6,000 bounding boxes (exactly one per image) are carried over unchanged** — no coordinate was altered. 6 classes ×1,000 each: `left_turn`, `straight_ahead`, `right_turn`, `dead_end`, `no_entry`, `stop`.

#### 🛣️ RoadCrack_DL_HY-corrected — 2,189 images · 2,677 boxes

DOI: [10.57967/hf/10896](https://doi.org/10.57967/hf/10896)

Pavement crack detection (transverse / alligator / longitudinal / sealed), 4 classes, Pascal VOC + YOLO annotations, box-level only. Non-commercial research use only. Cleaned, split and standardized **box-level** version of the **CrackDataset_DL_HY** pavement crack database (Huyan & Li et al.; **NON-COMMERCIAL RESEARCH USE ONLY**, Copyright Wei Li Research Team, Chang'An University): only the `BoxLevel_Detection` portion is included (the pixel-level `SematicSeg_Dataset` and the bundled label tools are excluded); the misspelled category **`transeverse`** (240 boxes) was merged into `transverse`; **138 empty annotations**, **60 unannotated images**, and the **7 images left empty after removing 12 out-of-range boxes** were dropped; **44 byte-identical duplicate images** were removed; perceptually near-identical vehicle-capture frames were grouped so each cluster stays on one side of a seeded, class-stratified **70/15/15** split (upstream has none); the GBK-mojibake `<folder>` values and the wrong hard-coded `<path>` were cleaned; and Pascal VOC XML + YOLO TXT annotations, `classes.txt`, `data.yaml` and CSVs were generated. **All 2,677 valid bounding boxes are carried over unchanged** — no coordinate was altered. 4 classes: `transverse` (1,069), `alligator` (597), `longitudinal` (585), `sealed` (426).

#### 🧱 VisuCeram_500x500-corrected — 3,264 images · 6,042 boxes

DOI: [10.57967/hf/10884](https://doi.org/10.57967/hf/10884)

Sanitary-ware ceramic surface defect detection (spot / body crack / glaze crack / crawling / pinhole / sign / no-defect), 7 classes, Pascal VOC + YOLO annotations, Apache-2.0. Cleaned, split and standardized version of the **VisuCeram 500x500** sanitary-ware ceramic surface defect dataset (Azad & Nahid, *IEEE* 2025; upstream [Md-Ali-Azad/VisuCeram](https://github.com/Md-Ali-Azad/VisuCeram); licensed **Apache-2.0**): **15 out-of-range boxes** (normalised centre up to 1.65 — placed outside the frame) were removed, and the 1 image left with no boxes was dropped; the per-class folder layout was **flattened** into a single image/label pool (a single image may hold boxes of several classes); a seeded, class-stratified **70/15/15** split was added (upstream has none); three perceptually near-identical pairs were kept on one side of the split; and Pascal VOC XML + YOLO TXT annotations, `classes.txt`, `data.yaml` and CSVs were generated. **All 6,042 valid bounding boxes are carried over unchanged** — no valid coordinate was altered. 7 classes: `spot` (2,030), `body_crack` (997), `glaze_crack` (973), `no_defect` (548), `crawling` (532), `pinhole` (509), `sign` (453). (In the upstream scheme `no_defect` is itself an annotated category, kept verbatim.)

#### ☀️ PV_Multi_Defect-corrected — 1,044 images · 3,403 boxes

DOI: [10.57967/hf/10882](https://doi.org/10.57967/hf/10882)

Photovoltaic panel multi-defect detection (hot spot / scratch / border / non-electricity / broken), 5 classes, Pascal VOC + YOLO annotations, with a near-duplicate-aware split. Cleaned, split and standardized version of the **PV-Multi-Defect** photovoltaic panel defect dataset (Li, Wang & Zhang, *Electronics* 2023, DOI 10.3390/electronics12030561; upstream [houhou34/PV-Multi-Defect](https://github.com/houhou34/PV-Multi-Defect); upstream licence unstated): **61 byte-identical duplicate images** (61 pairs) were removed; **2 unannotated images** (`img3059`, `img9513`) and **1 empty annotation** (`img7863`) were dropped; the single near-duplicate cluster (12 perceptually identical images) was grouped so it stays on one side of a seeded, class-stratified **70/15/15** split (upstream had none); the VOC metadata was cleaned (a bogus `<folder>` value `new`/`result2` and a hard-coded personal Windows `<path>` such as `C:\Users\86151\Desktop\\...`); and YOLO TXT annotations, `classes.txt`, `data.yaml` and CSVs were generated. **All 3,403 bounding boxes are carried over unchanged** — no coordinate was scaled, shifted or re-guessed. 5 classes: `hot_spot` (1,553), `scratch` (1,349), `black_border` (251), `no_electricity` (158), `broken` (92).

#### 🔥 DBA_Fire_Smoke-corrected — 3,846 images · 7,988 boxes

DOI: [10.57967/hf/10880](https://doi.org/10.57967/hf/10880)

Fire and smoke detection (flame / smoke), 2 classes, Pascal VOC + YOLO annotations, with a near-duplicate-aware split. Cleaned, de-duplicated, split and standardized version of the **DBA-Fire** fire and smoke detection dataset (reference paper: *DBA-YOLO: A Lightweight Fire Detection Algorithm with Structural Reparameterized Multiple Attention Mechanisms*; upstream licence unstated): **59 byte-identical duplicate images** (57 groups) were removed; because many images are perceptually near-identical (consecutive video frames plus re-encoded copies), each of the **3,014 near-duplicate clusters** (largest 87 images; 1,028 images live in multi-image clusters) was assigned **entirely to one split** so near-identical content never straddles train/val/test; **521 filenames** containing spaces/parentheses were normalised to `[A-Za-z0-9._-]`; a seeded, class-stratified **70/15/15** split was added (upstream had none); and Pascal VOC XML + YOLO TXT annotations, `classes.txt`, `data.yaml` and CSVs were generated. **All 7,988 bounding boxes are carried over unchanged** — no coordinate was scaled, shifted or re-guessed.

#### ⚡ CPLID_Insulators-corrected — 845 images · 1,566 boxes

DOI: [10.57967/hf/10878](https://doi.org/10.57967/hf/10878)

Power-line insulator defect detection (insulator / defect), 2 classes, Pascal VOC + YOLO annotations, with a burst-frame-aware split. Cleaned, split and standardized version of the **Chinese Power Line Insulator Dataset (CPLID)** (Tao et al., *IEEE TSMC: Systems* 2018; images provided by the State Grid Corporation of China, assembled by WANG Zi-Hao; upstream [InsulatorData/InsulatorDataSet](https://github.com/InsulatorData/InsulatorDataSet)): **3 pixel-identical duplicate images** in `Normal_Insulators` were removed (`0150`=`2984`, `0852`=`1876`, `1608`=`1938`); because the 600 normal images are **UAV video frames**, consecutive captures were grouped into **486 frame chains** and each chain assigned entirely to one split so no near-identical burst straddles train/val/test; the two parallel defective-insulator label folders (`labels/defect/` + `labels/insulator/`) were **merged into one annotation per image** (insulator box + defect box); a seeded, class-stratified **70/15/15** split was added (upstream had none); the VOC metadata was cleaned (bogus `<folder>` values `images`/`long`/empty, and a hard-coded local `<path>` leaking personal absolute paths with Chinese characters); a stray 48-byte non-image file (`OriginalImageOnWebDriver`) was removed; and Pascal VOC + YOLO annotations, `classes.txt`, `data.yaml` and CSVs were added. **All 1,566 bounding boxes are carried over unchanged** — no coordinate was scaled, shifted or re-guessed. Note: the **defective** images are **synthetic** (TVSeg + U-Net pipeline, as described upstream). Upstream licence unstated.

#### 🌱 PlantDoc-corrected — 2,565 images · 8,887 boxes

DOI: [10.57967/hf/10678](https://doi.org/10.57967/hf/10678)

Plant leaf disease detection across 13 crops, 29 classes, Pascal VOC + YOLO annotations, with train/test leakage removed. Cleaned version of the **PlantDoc** object-detection dataset (Singh et al., CoDS-COMAD 2020, [doi:10.1145/3371158.3371196](https://doi.org/10.1145/3371158.3371196), CC BY 4.0): **12 images were byte-identical between `TRAIN/` and `TEST/`** — a hard train/test leak — and were removed; 11 images shipped with an **empty XML** (no `<object>`) and 11 more with **no XML at all** were dropped; 4 images downloaded only as low-resolution thumbnails while annotated at original resolution (so their boxes lie outside the frame) were dropped, as was 1 orphan XML; **35 images carried an EXIF orientation tag** while their boxes had been authored against the stored pixel orientation — 30 received a byte-level tag strip (pixels untouched) and 5 had the EXIF rotation baked into the pixels, so the annotation canvas now matches the stored pixels under every loader (PIL, OpenCV, Ultralytics); 4 VOC files declaring `<width>0</width><height>0</height>` were repaired; **all 234 URL-tainted filenames** (`%20`, `+`, `?itok=`, `%253E`, 25 extension-less files and 12 with script extensions such as `.ashx`) were sanitised, and scraped SEO names running up to 215 characters were truncated to ≤80 characters plus an 8-hex-digit hash of the upstream name; all **29 class names** were normalised to Title Case (fixing the `Soyabean` typo); and a reproducible split was added — the official `TEST/` (236) is kept as **test** for paper comparability while a stratified 10 % **val** (233) is carved out of `TRAIN/` (seed 42). **All 8,887 bounding boxes are carried over unchanged** — no coordinate was scaled, shifted or re-guessed.

#### 🖥️ PCB_AoI_KubeEdge-corrected — 233 images · 1,011 boxes

DOI: [10.57967/hf/10677](https://doi.org/10.57967/hf/10677)

PCB AOI defect detection, 2 classes, Pascal VOC + YOLO annotations, with a de-duplicated training-only augmentation set. Cleaned version of the **PCB-AoI Public Dataset** (KubeEdge-Ianvs, by KubeEdge SIG AI members from China Telecom and Raisecom Technology): the upstream `train_data_augmentation/` silently mixed the 173 original tiles with their geometric transforms — here the originals are dropped (they remain in the core split) and the transforms moved to a dedicated `augmented/` folder, and the 156 transforms derived from val-split tiles were removed so the augmented set can never leak validation content; a seeded, class-stratified train/val/test split (147 / 26 / 60) was added; Pascal VOC + YOLO annotations were provided; and the upstream VOC metadata (bogus `UAV autolanding` folder/source/owner, and `.jpg` names for `.jpeg` files) was fixed. No bounding box was modified. Upstream licence unstated.

#### 🧲 MagneticTile-corrected — 1,318 images · 437 boxes

DOI: [10.57967/hf/10659](https://doi.org/10.57967/hf/10659)

Magnetic tile surface defects, 5 classes, Pascal VOC + YOLO annotations, with burst-shot duplicates removed. Cleaned and bounding-box standardized version of the **Magnetic Tile Surface Defect Dataset** (Huang, Qiu & Yuan, [arXiv:1805.01168](https://arxiv.org/abs/1805.01168), 2018): upstream ships only grayscale saliency masks and **no bounding boxes**, so 437 tight boxes were extracted for the 5 defect classes via adaptive Otsu thresholding; **22 burst-shot near-duplicate frames** were isolated (sub-second industrial camera repeats, MAE 1.64–4.14) to remove train/test leakage; 4 images in `MT_Uneven` carrying 100 % black masks were removed; and a seeded stratified 70/10/20 split was added. CC BY 4.0.

#### 🔧 PKU-Market-PCB-corrected — 693 images · 2,953 boxes

DOI: [10.57967/hf/10554](https://doi.org/10.57967/hf/10554)

PCB defect detection, 6 classes, COCO + Pascal VOC + YOLO annotations, board-disjoint split. Cleaned version of **PKU-Market-PCB** (Huang & Wei, [arXiv:1901.08204](https://arxiv.org/abs/1901.08204), 2019): a stray `data.yaml` was removed; Pascal VOC and YOLO annotations were added; and a **board-disjoint split** (541 / 152) was added because the upstream split places all 10 base boards in both halves (100 % board-level leakage — a model evaluated on it sees boards it has memorized). No bounding box was modified. Upstream licence unstated.

#### 🔌 DeepPCB-corrected — 1,499 images · 10,004 boxes

DOI: [10.57967/hf/10551](https://doi.org/10.57967/hf/10551)

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
