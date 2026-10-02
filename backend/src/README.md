# CatDog Vision Classifier - Backend Source

## Overview
Backend source code for the CatDog Vision Classifier application.

## Project Structure

```
backend/src/
├── routes/
│   └── classify.py      # Classification endpoint
├── services/
│   ├── model.py         # ML model inference
│   └── preprocessing.py # Image preprocessing
└── utils/
    ├── validation.py    # File validation
    └── response.py      # Response formatting
```

## Files

### routes/classify.py
API endpoint for image classification.

### services/model.py
ML model loading and inference.

### services/preprocessing.py
Image preprocessing pipeline.

### utils/validation.py
File upload validation.

### utils/response.py
Response formatting utilities.
