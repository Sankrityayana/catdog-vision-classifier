# CatDog Vision Classifier - Frontend Utils

## Overview
Utility functions for the CatDog Vision Classifier frontend.

## Utilities

### api.js
API communication utilities.

**Functions:**
- `classifyImage(file)`: Upload image for classification
- `handleError(error)`: Handle API errors
- `formatResponse(data)`: Format API response

## Usage

```javascript
import { classifyImage, handleError } from './utils/api';

try {
  const result = await classifyImage(imageFile);
} catch (error) {
  handleError(error);
}
```
