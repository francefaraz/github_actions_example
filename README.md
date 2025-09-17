# My Project

A full-stack application with React frontend and Flask backend.

## Project Structure

```
my-project/
├─ backend/
│  ├─ app.py                 # Flask application
│  ├─ requirements.txt       # Python dependencies
│  ├─ Dockerfile.backend     # Backend Docker configuration
│  └─ tests/                 # Backend tests
├─ frontend/
│  ├─ src/                   # React source code
│  ├─ public/                # Static assets
│  ├─ package.json           # Node.js dependencies
│  └─ vite.config.js         # Vite configuration
├─ .gitignore               # Git ignore rules
├─ .dockerignore            # Docker ignore rules
└─ README.md                # This file
```

## Features

### Backend (Flask)
- RESTful API endpoints
- CORS enabled for frontend integration
- Health check endpoint
- Docker support with Gunicorn
- Production-ready configuration

### Frontend (React + Vite)
- Modern React with hooks
- Vite for fast development and building
- ESLint configuration
- Hot Module Replacement (HMR)

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 16+
- Docker (optional)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python app.py
   ```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`

### Docker Setup

#### Backend
```bash
cd backend
docker build -f Dockerfile.backend -t my-project-backend .
docker run -p 5000:5000 my-project-backend
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/data` - Get sample data
- `POST /api/data` - Create new data

## Development

### Running Tests
```bash
cd backend
pytest
```

### Building for Production
```bash
# Frontend
cd frontend
npm run build

# Backend
cd backend
# Use Docker or deploy with Gunicorn
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
