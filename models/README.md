# CatDog Vision Classifier - Models

## Overview
This directory contains trained machine learning models for cat vs dog classification.

## Model Files
- `catdog_model.h5` - Trained Keras model
- `catdog_model.pt` - Trained PyTorch model
- `catdog_model.pkl` - Scikit-learn model

## Model Information
- **Input Size**: 224x224x3 (RGB)
- **Output**: 3 classes (cat, dog, unrelated)
- **Architecture**: CNN (Convolutional Neural Network)

## Usage
Models are loaded by the backend service for inference.

## Training
Training scripts are located in the `training/` directory (if applicable).
