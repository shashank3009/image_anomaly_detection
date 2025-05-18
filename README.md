# Image Anomaly Detection

This repository is dedicated to experiment with multiple **Image Anomaly Detection** techniques in PyTorch. It is structured to accommodate multiple models like **PaDiM**, and more to be added progressively.

This repository is built using the work from [Open Edge Platform's anomalib](https://github.com/open-edge-platform/anomalib). Their modular, research-friendly implementation laid the foundation for this work.

## Models Included

- [PaDiM (Patch Distribution Modeling)]() — [Paper](https://arxiv.org/abs/2011.08785)  
  → Implements training and inference on MVTec AD dataset  
  → [README](./PaDiM/README.md)

##  Dataset

I have used the [MVTec AD dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad), a widely used benchmark for industrial anomaly detection. 

## Citations

```bibtex
@inproceedings{defard2021padim,
  title={PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization},
  author={Defard, Thomas and Setkov, Alexandr and Loesch, Angelique and Audigier, Romain},
  booktitle={International Conference on Pattern Recognition (ICPR)},
  year={2020}
}

@misc{anomalib,
  author       = {Open Edge Platform Contributors},
  title        = {anomalib: A Library for Deep Learning-based Visual Anomaly Detection},
  howpublished = {\url{https://github.com/open-edge-platform/anomalib}},
  year         = {2021}
}


