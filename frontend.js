// CatDog Vision Classifier Frontend
// Connects to FastAPI backend at http://localhost:8000

// Configuration
const API_URL = 'http://localhost:8000/api/classify';
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp'];

// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const imagePreview = document.getElementById('imagePreview');
const actionSection = document.getElementById('actionSection');
const uploadBtn = document.getElementById('uploadBtn');
const clearBtn = document.getElementById('clearBtn');
const loadingSection = document.getElementById('loadingSection');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const errorMessage = document.getElementById('errorMessage');

// State
let selectedFile = null;
let previewUrl = null;

// Initialize
function init() {
    // Upload area click
    uploadArea.addEventListener('click', (e) => {
        if (e.target !== fileInput) {
            fileInput.click();
        }
    });

    // File input change
    fileInput.addEventListener('change', handleFileSelect);

    // Drag and drop events
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('drag-over');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('drag-over');
    });

    uploadArea.addEventListener('drop', handleDrop);

    // Upload button
    uploadBtn.addEventListener('click', handleUpload);

    // Clear button
    clearBtn.addEventListener('click', resetForm);
}

// Handle file selection via file picker
function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) validateAndPreviewFile(file);
}

// Handle drag and drop
function handleDrop(e) {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        validateAndPreviewFile(file);
    } else if (file) {
        showError('Please select a valid image file (JPG, PNG, or WEBP)');
    }
}

// Validate and preview file
function validateAndPreviewFile(file) {
    // Validate file type
    const isValidType = ALLOWED_TYPES.includes(file.type);
    if (!isValidType) {
        showError('Invalid file type. Please use JPG, PNG, or WEBP format.');
        return;
    }

    // Validate file size
    if (file.size > MAX_FILE_SIZE) {
        showError('File size exceeds 5MB limit. Please select a smaller image.');
        return;
    }

    // Reset errors
    hideError();

    // Store file
    selectedFile = file;

    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewUrl = e.target.result;
        imagePreview.src = previewUrl;
        previewSection.style.display = 'block';
        actionSection.style.display = 'block';
        uploadBtn.disabled = false;
    };
    reader.readAsDataURL(file);
}

// Handle upload
async function handleUpload() {
    if (!selectedFile) {
        showError('No file selected. Please select an image first.');
        return;
    }

    // Reset UI
    hideError();
    resultsSection.style.display = 'none';
    loadingSection.style.display = 'block';

    try {
        // Create form data
        const formData = new FormData();
        formData.append('image', selectedFile);

        // Make API call
        const response = await fetch(API_URL, {
            method: 'POST',
            body: formData,
        });

        // Check response
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `API error: ${response.status} ${response.statusText}`);
        }

        // Parse result
        const result = await response.json();
        displayResult(result);

    } catch (error) {
        showError(error.message || 'Failed to classify image. Please try again.');
    } finally {
        loadingSection.style.display = 'none';
    }
}

// Display classification result
function displayResult(result) {
    // Determine prediction and confidence
    const prediction = result.prediction || 'Unknown';
    const confidence = result.confidence ? `${(result.confidence * 100).toFixed(2)}%` : '-';
    
    // Format details
    let details = '';
    if (result.details) {
        details = JSON.stringify(result.details, null, 2);
    } else if (result.class_name) {
        details = result.class_name;
    }

    // Update UI
    document.getElementById('prediction').textContent = prediction;
    document.getElementById('confidence').textContent = confidence;
    document.getElementById('details').textContent = details;

    // Show results
    resultsSection.style.display = 'block';
}

// Reset form
function resetForm() {
    selectedFile = null;
    previewUrl = null;
    fileInput.value = '';
    
    imagePreview.src = '';
    previewSection.style.display = 'none';
    actionSection.style.display = 'none';
    resultsSection.style.display = 'none';
    loadingSection.style.display = 'none';
    hideError();
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
}

// Hide error message
function hideError() {
    errorSection.style.display = 'none';
    errorMessage.textContent = '';
}

// Initialize on load
document.addEventListener('DOMContentLoaded', init);
