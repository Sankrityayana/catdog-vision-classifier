# CatDog Vision Classifier - Backend Routes

## Overview
API routes for the CatDog Vision Classifier backend.

## Routes

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

## Error Responses

### 400 Bad Request
Invalid file format or empty file.

### 413 Payload Too Large
File size exceeds maximum limit.

### 500 Internal Server Error
Model inference failed.
