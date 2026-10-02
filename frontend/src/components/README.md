# CatDog Vision Classifier - Frontend Components

## Overview
React components for the CatDog Vision Classifier frontend.

## Components

### UploadForm.js
Image upload form component.

**Features:**
- File selection
- Drag and drop support
- File validation
- Upload button

### ResultDisplay.js
Result display component with confidence scores.

**Features:**
- Classification result
- Confidence percentage
- Visual indicators

### LoadingSpinner.js
Loading indicator component.

**Features:**
- Animated spinner
- Loading message

## Usage

```jsx
import UploadForm from './components/UploadForm';
import ResultDisplay from './components/ResultDisplay';

function App() {
  return (
    <div>
      <UploadForm />
      <ResultDisplay />
    </div>
  );
}
```
