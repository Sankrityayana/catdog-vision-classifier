# CatDog Vision Classifier

A single-user web application for image classification that determines whether an uploaded photograph contains a **cat**, **dog**, or **unrelated object**.

## Overview

**CatDog Vision Classifier** is an educational web application that demonstrates the integration of a computer vision classification model into a complete web application pipeline.

### Project Type
- **Category**: University/Class Project
- **Focus**: Computer Vision, Image Classification, Machine Learning, Web Application Development
- **Scope**: Single-user, local development and execution

## Features

### Core Functionality
- 📷 Image upload through web interface
- 🐱 Cat vs Dog classification using trained ML model
- 🚫 Unrelated object detection and rejection
- 📊 Confidence scoring and result display
- ✅ File format and size validation
- 🖼️ Image preprocessing for model input

### Technical Stack
- **Backend**: Python (Flask/FastAPI)
- **Frontend**: HTML/CSS/JavaScript (Vanilla or React)
- **ML/DL**: PyTorch/TensorFlow/Keras
- **Image Processing**: OpenCV/Pillow
- **Deployment**: Local development environment

## Project Structure

```
catdog-vision-classifier/
├── backend/              # Backend API server
│   ├── src/
│   │   ├── routes/      # API endpoints
│   │   ├── services/    # Business logic
│   │   └── utils/       # Helper functions
│   ├── requirements.txt
│   └── app.py
├── frontend/            # Web interface
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── utils/
│   ├── public/
│   └── index.html
├── models/              # Trained ML models
│   ├── catdog_model.h5  # Example model file
│   └── README.md
├── data/               # Training/validation data
│   ├── train/
│   ├── val/
│   └── README.md
├── tests/              # Unit and integration tests
│   ├── test_backend/
│   └── test_frontend/
├── Docs/               # Project documentation
├── .gitignore
├── requirements.txt
└── README.md
```

## Implementation Phases

### Phase 1: Project Setup & Infrastructure
- [ ] Initialize Git repository
- [ ] Set up project structure
- [ ] Configure development environment
- [ ] Create documentation structure
- [ ] Set up CI/CD pipeline (optional)

### Phase 2: Backend Development
- [ ] Set up Flask/FastAPI server
- [ ] Implement image upload endpoint
- [ ] Create file validation utilities
- [ ] Implement preprocessing module
- [ ] Integrate ML model inference
- [ ] Add result formatting and confidence scoring
- [ ] Implement error handling for unrelated objects

### Phase 3: Frontend Development
- [ ] Create HTML/CSS structure
- [ ] Implement image upload interface
- [ ] Add loading states and progress indicators
- [ ] Create result display component
- [ ] Implement error message handling
- [ ] Add responsive design

### Phase 4: ML Model Integration
- [ ] Select/pretrain classification model
- [ ] Implement preprocessing pipeline
- [ ] Create classification service
- [ ] Add unrelated object detection
- [ ] Optimize inference performance

### Phase 5: Testing & Validation
- [ ] Write unit tests for backend
- [ ] Write integration tests
- [ ] Test with various image formats
- [ ] Validate unrelated object detection
- [ ] Performance testing

### Phase 6: Documentation & Deployment
- [ ] Complete project documentation
- [ ] Create user guide
- [ ] Document model architecture
- [ ] Prepare deployment instructions
- [ ] Final testing and review

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend)
- pip or conda package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd catdog-vision-classifier
```

2. Set up backend:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up frontend:
```bash
cd ../frontend
npm install
```

4. Run the application:
```bash
# Backend
cd backend
python app.py

# Frontend (in separate terminal)
cd frontend
npm start
```

## Project Goals

1. Demonstrate complete image classification pipeline
2. Show integration of ML models with web applications
3. Implement proper validation and error handling
4. Create user-friendly interface
5. Document the entire development process

## License

This project is for educational purposes.

## Author

Project for university/class demonstration.
