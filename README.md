# Flow Zoometry Code Suites

This repository contains software relevant to **flow zoometry**.  
It comprises three major components:

- **Tissue segmentation** — high-accuracy pre-trained segmentation models for *Drosophila* larval internal tissues & body. 
- **PDAC drug screening classifier** — ensemble 3D-CNN models for PDAC tumor model fly classification & drug efficacy evaluation.
- **LabVIEW integrated control system** — hardware automation for 3D imaging of cleared *Drosophila* larvae.

> 📄 For methodology and experimental details, please refer to the preprint:  
> [bioRxiv: 10.1101/2024.04.04.588032v1](https://www.biorxiv.org/content/10.1101/2024.04.04.588032v1)

---

## 📁 Repository Structure
```
.
├── src/flyseg                  # Drosophila tissue segmentation (based on nnUNet v2 structure)
├── Flyscreening/        # PDAC cancer model classification & drug screening (3D-CNN ensemble classification)
├── LCIS/         # LabVIEW integrated control system for imaging hardware control
└── README.md                # Instruction documentation (this file)
```

> Each subdirectory contains its own **README.md** for setup and usage instructions.

---

## ① FlySeg — Drosophila tissue segmentation (nnUNet v2)

### Overview
**FlySeg** is a modular, pre-trained segmentation pipeline designed for *Drosophila* larval tissue segmentation using the **nnUNet v2** framework.  
It automates 3D fluorescence image processing, segmentation, and statistical quantification with high reproducibility and accuracy.

### Supported Tissues
The flyseg model currently support high-accuracy segmentation for the following larval tissues:
- **Central nervous system (CNS)**  
- **Wing disc (left and right)**  
- **Haltere disc (left and right)**  
- **Salivary gland (left and right)**  
- **Proventriculus**  
- **Body (whole contour)**  

### Example Visualizations
<p align="center">
  <img src="src/Segmentation%20cases/7%20tissue%20segmentation%20case.png" width="600"/>
  <img src="src/Segmentation%20cases/CNS%20segmentation%20case.png" width="600"/>
  <img src="src/Segmentation%20cases/Body%20case.png" width="600"/>
</p>

### Typical Workflow
1. Convert `.h5` 3D imaging data into nnUNet-compatible format.  
2. Run segmentation using pre-trained tissue-specific models.  
3. Generate `.nii.gz` masks and extract volumetric/morphological statistics.

> See `FlySeg/README.md` for installation, pretrained weights, and command examples.

---

## ② FlyDrugScreening — PDAC drug candidate efficacy classification (3D-CNN)

### Overview
**FlyDrugScreening** provides a 3D convolutional neural network (3D-CNN)–based framework to quantify tumor morphology and evaluate drug efficacy in a *Drosophila* PDAC (pancreatic ductal adenocarcinoma) model.  
The system performs **ensemble inference** using 23 trained **MC3-18** models to compute the **probability of cancer morphology classness**.

- **Lower ensemble score → Effective drug response (tumor regression)**  
- **Higher ensemble score → Persistent or progressive tumor state**

### Folder Structure
```
FlyDrugScreening/
├── DrugScreening.py             # Main inference script
├── requirements.txt             # Dependency list
├── samples/                     # Example test volumes (.h5)
│   ├── sample_001.h5
│   └── ...
└── models/                      # Trained 3D-CNN weights (.tar)
    ├── best_model_for_date_20231114.tar
    ├── ...
    └── best_model_for_date_20241017.tar
```

### Input & Output
- **Input:** `.h5` file, dataset name `dataset_1`  
- **Output:** `test_result.csv` example:
  ```
  File Name,Probability of Classness to Cancer Morphology
  samples/sample_001.h5,0.9321
  samples/sample_002.h5,0.1485
  ```

> 📄 Detailed model loading, ensemble weighting, and visualization are described in `FlyDrugScreening/README.md`.

---

## ③ LabVIEW Integrated Control System

### Overview
A **LabView-based graphical control system** enabling real-time automation and synchronization of multiple imaging hardware components.

### Integrated Modules
- **Laser** – wavelength and power modulation  
- **Camera** – acquisition triggering and synchronization  
- **ETL (Electrotunable lens)** – dynamic focal plane adjustment  
- **Pump** – fluidic control and timing  
- **Stage** – motorized positioning system  
- **Robot arm** – automated sample handling
- **Filter** – automated filter switch and multi-color imaging

### Features
- Unified hardware control with synchronized timing  
- Real-time logging and metadata recording  
- Modular architecture for easy extension to new devices  

> 🔧 For environment setup, hardware requirements, and workflow configuration, see `LabVIEW-Control/README.md`.

---

## 📬 Contact

- **Code Maintainer:** Walker Peterson, Chenglang Hu, Md Al Mehedi Hasan
- **Email:** peterson@flyworks.co.jp  
- **Issues & Contributions:** please cite our paper if you use the code herein.
bioRxiv: 10.1101/2024.04.04.588032v1](https://www.biorxiv.org/content/10.1101/2024.04.04.588032v1)

