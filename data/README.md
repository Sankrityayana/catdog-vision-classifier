# CatDog Vision Classifier - Data

## Overview
This directory contains training and validation data for the ML model.

## Directory Structure

```
data/
├── train/           # Training data
│   ├── cat/        # Cat images
│   └── dog/        # Dog images
├── val/            # Validation data
│   ├── cat/
│   └── dog/
└── test/           # Test data (unrelated objects)
    └── unrelated/
```

## Data Requirements
- **Image Format**: JPG, PNG
- **Minimum Size**: 224x224 pixels
- **Augmentation**: Rotation, flipping, zooming

## Dataset Sources
- Kaggle Cat vs Dog dataset
- Custom collected images
- Data augmentation
