"""
CatDog Vision Classifier - FastAPI Backend

A single-file FastAPI application for cat/dog image classification
with unrelated object detection.
"""

import io
import os
from typing import Dict, Any

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import torch

from model import (
    get_model,
    get_preprocessing_transforms,
    classify_image,
    CONFIDENCE_THRESHOLD,
    CLASS_NAMES,
    IMAGENET_MEAN,
    IMAGENET_STD
)

# Initialize FastAPI app
app = FastAPI(
    title="CatDog Vision Classifier",
    description="API for classifying cat and dog images with unrelated object detection"
)

# Configuration
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Initialize model and preprocessing transforms
model = get_model()
transform = get_preprocessing_transforms()

def allowed_file(filename: str) -> bool:
    """Check if file extension is allowed."""
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def validate_file_size(file: UploadFile) -> None:
    """Validate file size is within limits."""
    file.file.seek(0, io.SEEK_END)
    file_size = file.file.tell()
    file.file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds 5MB limit. Current size: {file_size / (1024*1024):.2f}MB"
        )

def preprocess_image(file_content: bytes) -> torch.Tensor:
    """Preprocess image for model inference using model.py transforms."""
    image = Image.open(io.BytesIO(file_content)).convert("RGB")
    return transform(image).unsqueeze(0)

def classify_image(image_tensor: torch.Tensor) -> Dict[str, Any]:
    """Classify image using model.py classify_image function."""
    return classify_image(model, image_tensor, CONFIDENCE_THRESHOLD)

@app.post("/api/classify")
async def classify_image_endpoint(file: UploadFile = File(...)) -> JSONResponse:
    """
    Classify an uploaded image as cat, dog, or unrelated object.
    
    Args:
        file: Uploaded image file (JPG, PNG, or WEBP)
    
    Returns:
        JSON response with classification results
    """
    # Validate file extension
    if not allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Validate file size
    validate_file_size(file)
    
    # Read file content
    file_content = await file.read()
    
    try:
        # Preprocess image
        image_tensor = preprocess_image(file_content)
        
        # Classify
        result = classify_image(image_tensor)
        
        # Check confidence threshold for unrelated object detection
        if result["confidence"] < CONFIDENCE_THRESHOLD:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": "Unrelated object detected",
                    "message": f"The uploaded image does not appear to be a cat or dog. "
                              f"Maximum confidence: {result['confidence']:.2%}",
                    "details": result
                }
            )
        
        # Return successful classification
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "classification": result["class"],
                "confidence": result["confidence"],
                "message": f"Image classified as {result['class']} with {result['confidence']:.2%} confidence",
                "details": result
            }
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during classification: {str(e)}"
        )

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint with API information."""
    return {
        "name": "CatDog Vision Classifier",
        "version": "1.0.0",
        "endpoints": {
            "classify": "/api/classify (POST)"
        },
        "validation": {
            "allowed_formats": list(ALLOWED_EXTENSIONS),
            "max_file_size_mb": MAX_FILE_SIZE / (1024 * 1024),
            "confidence_threshold": CONFIDENCE_THRESHOLD
        }
    }

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
