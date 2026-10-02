# CatDog Vision Classifier - Backend Utils

## Overview
Utility functions for the CatDog Vision Classifier backend.

## Utilities

### validation.py
File upload validation.

**Functions:**
- `validate_file(file)`: Validate uploaded file
- `check_file_size(file, max_size)`: Check file size
- `check_file_format(file, allowed_formats)`: Check file format

### response.py
Response formatting utilities.

**Functions:**
- `success_response(data)`: Format success response
- `error_response(message, status_code)`: Format error response
- `classification_response(classification, confidence)`: Format classification response

## Usage

```python
from utils.validation import validate_file, check_file_size
from utils.response import success_response, error_response

if not validate_file(file):
    return error_response("Invalid file format", 400)
```
