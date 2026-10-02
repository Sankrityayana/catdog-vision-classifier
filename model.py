"""
CatDog Vision Classifier - Model Module

This module handles all machine learning functionality including:
- Loading pretrained ResNet18 model with transfer learning
- Image preprocessing pipeline
- Confidence thresholding for unrelated object detection
- Classification inference
"""

import os
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from typing import Dict, Any, Tuple


# Configuration
CONFIDENCE_THRESHOLD = 0.70  # 70% minimum confidence for valid classification
CLASS_NAMES = ["cat", "dog"]
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


def get_preprocessing_transforms() -> transforms.Compose:
    """
    Create preprocessing transforms for image input.
    
    Returns:
        Compose transform with resize, tensor conversion, and normalization
    """
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=IMAGENET_MEAN,
            std=IMAGENET_STD
        )
    ])


def load_model() -> nn.Module:
    """
    Load pretrained ResNet18 model with transfer learning for cat/dog classification.
    
    The model uses ImageNet pretrained weights and replaces the final fully connected
    layer for binary classification (cat vs dog).
    
    Returns:
        Pretrained ResNet18 model modified for binary classification
    """
    # Load pretrained ResNet18 with ImageNet weights
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    
    # Freeze all layers - we'll use transfer learning with the pretrained features
    for param in model.parameters():
        param.requires_grad = False
    
    # Replace the final fully connected layer for binary classification
    num_features = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_features, 256),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(256, 2)  # Binary classification: cat or dog
    )
    
    return model


def get_model(model_path: str = "model.pth") -> nn.Module:
    """
    Load model with pretrained weights or from saved checkpoint.
    
    Args:
        model_path: Path to saved model weights (default: "model.pth")
    
    Returns:
        Loaded model ready for inference
    """
    model = load_model()
    
    # Try to load saved model weights
    try:
        if model_path and os.path.exists(model_path):
            model.load_state_dict(torch.load(model_path, map_location="cpu", weights_only=True))
            print(f"Loaded model from {model_path}")
        else:
            print("Using pretrained ResNet18 weights (model.pth not found)")
    except Exception as e:
        print(f"Warning: Could not load model from {model_path}: {e}")
        print("Using pretrained weights instead")
    
    model.eval()  # Set to evaluation mode
    return model


def preprocess_image(image_tensor: torch.Tensor) -> torch.Tensor:
    """
    Preprocess image tensor for model inference.
    
    This function applies the standard ImageNet normalization to the input tensor.
    
    Args:
        image_tensor: Input image tensor in [0, 1] range
    
    Returns:
        Normalized tensor ready for model inference
    """
    transform = get_preprocessing_transforms()
    return transform(image_tensor)


def classify_image(
    model: nn.Module, 
    image_tensor: torch.Tensor,
    confidence_threshold: float = CONFIDENCE_THRESHOLD
) -> Dict[str, Any]:
    """
    Classify an image and return results with confidence scores.
    
    Args:
        model: Trained classification model
        image_tensor: Preprocessed image tensor
        confidence_threshold: Minimum confidence for valid classification
    
    Returns:
        Dictionary with classification results including:
        - class: Predicted class name (cat/dog/unrelated)
        - confidence: Confidence score
        - probabilities: Dictionary of class probabilities
        - is_unrelated: Boolean indicating if image is unrelated
    """
    with torch.no_grad():
        # Get model outputs
        outputs = model(image_tensor)
        
        # Apply softmax to get probabilities
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        
        # Get confidence and predicted class
        confidence, predicted = torch.max(probabilities, 0)
        
        class_idx = predicted.item()
        class_name = CLASS_NAMES[class_idx]
        confidence_value = confidence.item()
        
        # Build result dictionary
        result = {
            "class": class_name,
            "confidence": round(confidence_value, 4),
            "probabilities": {
                "cat": round(probabilities[0].item(), 4),
                "dog": round(probabilities[1].item(), 4)
            },
            "is_unrelated": False
        }
        
        # Check if confidence is below threshold (unrelated object detection)
        if confidence_value < confidence_threshold:
            result["class"] = "unrelated"
            result["is_unrelated"] = True
        
        return result


def predict(
    model: nn.Module,
    image_tensor: torch.Tensor,
    confidence_threshold: float = CONFIDENCE_THRESHOLD
) -> Tuple[str, float, bool]:
    """
    Simple prediction interface.
    
    Args:
        model: Trained classification model
        image_tensor: Preprocessed image tensor
        confidence_threshold: Minimum confidence for valid classification
    
    Returns:
        Tuple of (predicted_class, confidence, is_unrelated)
    """
    result = classify_image(model, image_tensor, confidence_threshold)
    return result["class"], result["confidence"], result["is_unrelated"]
