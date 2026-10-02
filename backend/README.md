# CatDog Vision Classifier - Backend

## Overview
Backend API server for the CatDog Vision Classifier application.

## Tech Stack
- **Framework**: Flask/FastAPI
- **ML Framework**: PyTorch/TensorFlow/Keras
- **Image Processing**: OpenCV/Pillow

## Setup

```bash
cd backend
pip install -r requirements.txt
```

## Running

```bash
python app.py
```

## API Endpoints

### POST /api/classify
Upload and classify an image.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: image file

**Response:**
```json
{
  "classification": "cat" | "dog" | "unrelated",
  "confidence": 0.95,
  "message": "Image classified successfully"
}
```

## Project Structure

```
backend/
├── src/
│   ├── routes/
│   │   └── classify.py      # Classification endpoint
│   ├── services/
│   │   ├── model.py         # ML model inference
│   │   └── preprocessing.py # Image preprocessing
│   └── utils/
│       ├── validation.py    # File validation
│       └── response.py      # Response formatting
├── app.py                   # Main application
├── requirements.txt
└── README.md
```
