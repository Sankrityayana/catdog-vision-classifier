# CatDog Vision Classifier - Testing Guide

## Overview

This document describes the testing strategy and procedures for the CatDog Vision Classifier application.

## Test Structure

```
tests/
├── test_backend/      # Backend tests
│   ├── test_routes/
│   │   └── test_classify.py
│   ├── test_services/
│   │   ├── test_model.py
│   │   └── test_preprocessing.py
│   └── test_utils/
│       ├── test_validation.py
│       └── test_response.py
└── test_frontend/     # Frontend tests
    ├── components/
    │   ├── test_UploadForm.js
    │   ├── test_ResultDisplay.js
    │   └── test_LoadingSpinner.js
    └── pages/
        └── test_Home.js
```

## Backend Testing

### Running Tests

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
pytest
```

### Test Categories

#### Unit Tests
- File validation
- Image preprocessing
- Model inference
- Response formatting

#### Integration Tests
- API endpoint testing
- End-to-end classification flow
- Error handling

### Test Coverage

- File upload validation
- Image preprocessing pipeline
- Model inference accuracy
- Error response formatting

## Frontend Testing

### Running Tests

```bash
cd frontend
npm test
```

### Test Categories

#### Component Tests
- UploadForm component
- ResultDisplay component
- LoadingSpinner component

#### Integration Tests
- Complete classification workflow
- Error handling in UI

### Test Coverage

- Form submission
- Result display
- Loading states
- Error messages

## Test Data

### Training Data
- Cat images: 1000+
- Dog images: 1000+

### Test Data
- Cat images: 200+
- Dog images: 200+
- Unrelated objects: 200+

## Continuous Integration

### GitHub Actions

The project uses GitHub Actions for CI/CD:

```yaml
name: CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
      - name: Run tests
        run: |
          cd backend
          pytest
```

## Test Results

### Coverage Report

Generate coverage report:

```bash
cd backend
pytest --cov=. --cov-report=html
```

View report in `htmlcov/index.html`

### Performance Tests

Test inference time:

```bash
cd backend
python -m timeit -s "from services.model import load_model, classify_image" "classify_image(load_model(), test_image)"
```

## Troubleshooting

### Test Failures

- Check dependencies are installed
- Verify test data is present
- Check model file path

### Coverage Issues

- Add tests for uncovered code paths
- Test edge cases and error conditions
