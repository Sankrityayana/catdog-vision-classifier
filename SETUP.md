# CatDog Vision Classifier - Setup Guide

## Prerequisites

- Python 3.8+
- Node.js 16+
- pip or conda package manager
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sankrityayana/catdog-vision-classifier.git
cd catdog-vision-classifier
```

### 2. Set Up Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Frontend

```bash
cd ../frontend
npm install
```

## Running the Application

### Development Mode

#### Backend

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

The backend server will start on `http://localhost:5000`

#### Frontend

```bash
cd frontend
npm start
```

The frontend will start on `http://localhost:3000`

### Production Mode

#### Backend

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Frontend

```bash
cd frontend
npm run build
npx serve -s dist
```

## Docker (Optional)

### Build Docker Image

```bash
docker build -t catdog-vision-classifier .
```

### Run Docker Container

```bash
docker run -p 5000:5000 catdog-vision-classifier
```

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
FLASK_ENV=development
FLASK_APP=app.py
MODEL_PATH=models/catdog_model.h5
MAX_FILE_SIZE=5242880  # 5MB in bytes
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif
```

## Troubleshooting

### Backend Issues

- **Import errors**: Ensure all dependencies are installed
- **Port already in use**: Change the port in `app.py`
- **Model loading errors**: Check model file path and format

### Frontend Issues

- **Module not found**: Run `npm install`
- **Port already in use**: Change the port in `vite.config.js`
- **API connection errors**: Check backend server is running

## Next Steps

1. Train or download a pre-trained model
2. Add training data to the `data/` directory
3. Run tests: `pytest` (backend) and `npm test` (frontend)
4. Deploy to production environment
