# CatDog Vision Classifier - Backend Services

## Overview
Business logic and ML model integration for the CatDog Vision Classifier.

## Services

### model.py
ML model loading and inference.

**Functions:**
- `load_model()`: Load trained model from file
- `classify_image(image)`: Classify an image
- `get_confidence()`: Get classification confidence

### preprocessing.py
Image preprocessing pipeline.

**Functions:**
- `preprocess_image(image)`: Preprocess image for model input
- `resize_image(image, size)`: Resize image to required dimensions
- `normalize_image(image)`: Normalize pixel values

## Usage

```python
from services.model import load_model, classify_image
from services.preprocessing import preprocess_image

model = load_model()
image = preprocess_image(user_image)
result = classify_image(model, image)
```
