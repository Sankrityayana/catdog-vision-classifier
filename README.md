# 🐱🐶 CatDog Vision Classifier

A single-user web application for image classification that determines whether an image contains a **cat**, **dog**, or an **unrelated object**.

This is a class project demonstrating fundamental concepts of computer vision, deep learning, and web application development.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-orange.svg)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.5+-red.svg)](https://pytorch.org/)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [API Documentation](#-api-documentation)
- [Frontend Usage](#-frontend-usage)
- [Project Structure](#-project-structure)
- [Limitations](#-limitations)

---

## ✨ Features

- **Cat vs Dog Classification**: Uses a pretrained ResNet18 model with transfer learning to classify images
- **Unrelated Object Detection**: Rejects images that don't contain cats or dogs (confidence threshold: 70%)
- **Web Interface**: Simple, responsive HTML/CSS/JS frontend with drag-and-drop support
- **File Validation**: Validates file types (JPG, PNG, WEBP) and sizes (max 5MB)
- **Confidence Scoring**: Shows prediction confidence for transparent results
- **Error Handling**: Clear error messages for invalid uploads and unrelated objects

---

## 🛠 Tech Stack

### Backend
- **FastAPI**: Modern Python web framework for the API
- **Uvicorn**: ASGI server for FastAPI
- **PyTorch**: Deep learning framework
- **TorchVision**: Computer vision utilities and pretrained models
- **Pillow**: Image processing library

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox
- **JavaScript (ES6+)**: Client-side logic and API integration

### Machine Learning
- **ResNet18**: Pretrained convolutional neural network
- **Transfer Learning**: Fine-tuned for binary classification (cat/dog)
- **ImageNet Preprocessing**: Standard normalization (mean: [0.485, 0.456, 0.406], std: [0.229, 0.224, 0.225])

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd /home/sankrityayana/Sankrityayana/Workspace-room/Project/catdog-vision-classifier
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the model weights** (if not already present)
   
   The project will use pretrained weights automatically if `model.pth` is not found. To train and save custom weights:
   ```bash
   python -c "from model import get_model; get_model('model.pth')"
   ```

---

## ▶️ How to Run

### Starting the Application

1. **Run the backend server**
   ```bash
   python backend.py
   ```

   You should see output like:
   ```
   INFO:     Started server process [12345]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
   ```

2. **Open the frontend**
   
   Open `frontend.html` in your web browser (Chrome, Firefox, Edge, or Safari recommended).

3. **Use the application**
   - Drag and drop an image onto the upload area, or click to select a file
   - Click "Upload Image" to classify
   - View the results and confidence score

### Stopping the Server

Press `CTRL+C` in the terminal where the server is running.

---

## 📡 API Documentation

### Base URL

```
http://localhost:8000
```

### POST /api/classify

Classify an uploaded image as cat, dog, or unrelated object.

#### Request

- **Content-Type**: `multipart/form-data`
- **File field**: `file` (JPG, PNG, or WEBP)

#### Success Response (200)

**Cat or Dog Classification:**
```json
{
  "success": true,
  "classification": "cat",
  "confidence": 0.92,
  "message": "Image classified as cat with 92.00% confidence",
  "details": {
    "class": "cat",
    "confidence": 0.92,
    "probabilities": {
      "cat": 0.92,
      "dog": 0.08
    }
  }
}
```

**Unrelated Object (confidence below threshold):**
```json
{
  "success": false,
  "classification": "unrelated",
  "confidence": 0.45,
  "message": "Image does not contain a cat or dog (confidence: 45.00%)",
  "details": {
    "class": "unrelated",
    "confidence": 0.45,
    "probabilities": {
      "cat": 0.30,
      "dog": 0.20
    }
  }
}
```

#### Error Responses

**Invalid File Type (400):**
```json
{
  "detail": "Invalid file type. Allowed types: .jpg, .jpeg, .png, .webp"
}
```

**File Too Large (413):**
```json
{
  "detail": "File size exceeds 5MB limit. Current size: 6.25MB"
}
```

**Image Processing Error (400):**
```json
{
  "detail": "Invalid image file. Please upload a valid image."
}
```

---

## 🖥️ Frontend Usage

### Uploading an Image

1. **Drag and Drop**: Drag an image file onto the upload area
2. **Click to Select**: Click the upload area to open the file picker
3. **Preview**: The image will be displayed in the preview section

### Classifying

1. After selecting an image, click the **"Upload Image"** button
2. Wait for the classification to complete (usually 1-3 seconds)
3. The results will appear in the results section

### Viewing Results

The application displays:
- **Prediction**: "Cat" or "Dog" (or "Unrelated" if confidence is low)
- **Confidence**: Percentage confidence score (e.g., "92.00%")
- **Details**: Full probability breakdown for both classes

### Clearing the Form

Click **"Clear"** to reset the form and upload a new image.

### Error Handling

If an error occurs (invalid file, unrelated object, etc.), an error message will appear at the bottom of the form.

---

## 📁 Project Structure

```
catdog-vision-classifier/
├── backend.py          # FastAPI backend server
├── frontend.html       # HTML frontend
├── frontend.css        # CSS styling
├── frontend.js         # JavaScript client-side logic
├── model.py            # Machine learning model and preprocessing
├── requirements.txt    # Python dependencies
├── model.pth           # Saved model weights (optional, auto-downloads)
└── README.md           # This file
```

### File Descriptions

| File | Description |
|------|-------------|
| `backend.py` | FastAPI server with `/api/classify` endpoint |
| `frontend.html` | HTML structure for the web interface |
| `frontend.css` | Styling for responsive layout |
| `frontend.js` | Client-side logic, file handling, API calls |
| `model.py` | PyTorch model, preprocessing, classification logic |
| `requirements.txt` | Python package dependencies |

---

## ⚠️ Limitations

### Model Limitations

- **Binary Classification**: Only distinguishes between cats and dogs; all other objects are classified as "unrelated"
- **Confidence Threshold**: 70% threshold may miss some valid classifications or incorrectly accept some unrelated objects
- **Image Quality**: Requires reasonably clear images; very blurry or low-resolution images may reduce accuracy
- **Lighting Conditions**: Extreme lighting (very dark or overexposed) may affect accuracy
- **Partial Objects**: Images with only partial cats/dogs (e.g., tail only) may not classify correctly

### Technical Limitations

- **Single User**: Not designed for concurrent users (use a production server for that)
- **Local Only**: Runs only on localhost; not deployed to a public server
- **File Size**: Limited to 5MB images
- **Format Support**: Only JPG, PNG, and WEBP formats
- **No Training Interface**: Model training must be done separately

### Performance

- **Inference Speed**: ~1-3 seconds on CPU; faster on GPU
- **Memory Usage**: ~500MB RAM for model loading
- **No Caching**: Each request processes the image independently

---

## 📚 Learning Objectives

This project demonstrates:

1. **Computer Vision**: Image preprocessing and feature extraction
2. **Deep Learning**: Transfer learning with ResNet18
3. **Web Development**: REST API with FastAPI
4. **Frontend Development**: HTML/CSS/JS with modern APIs (FileReader, Fetch)
5. **Model Inference**: Loading and using trained models
6. **Validation**: File type and size validation
7. **Error Handling**: Graceful handling of edge cases

---

## 🤝 Contributing

This is a class project. For educational purposes only.

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 👨‍🏫 Author

Class Project - CatDog Vision Classifier

---

## 🙏 Acknowledgments

- ResNet18 model from [TorchVision](https://pytorch.org/vision/stable/models.html)
- FastAPI framework from [Sebastián Ramírez](https://github.com/tiangolo)
- ImageNet pretrained weights

---

*Last updated: October 2026*
