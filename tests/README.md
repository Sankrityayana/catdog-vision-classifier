# CatDog Vision Classifier - Tests

## Overview
Unit and integration tests for the CatDog Vision Classifier application.

## Test Structure

```
tests/
├── test_backend/      # Backend tests
│   ├── test_routes/
│   ├── test_services/
│   └── test_utils/
└── test_frontend/     # Frontend tests
    ├── components/
    └── pages/
```

## Running Tests

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
```

## Test Coverage
- Image upload validation
- Model inference
- Result formatting
- Error handling
- Frontend components
