# Simple Backend CICD - Quote API

A simple FastAPI-based backend service that provides random inspirational quotes. This project demonstrates a basic API setup with Docker containerization and is designed for CI/CD pipeline integration.

## 🚀 Features

- **Random Quote API**: Get inspirational quotes from a curated collection
- **Health Check Endpoint**: Monitor service health
- **CORS Enabled**: Frontend-friendly with cross-origin support
- **Docker Ready**: Containerized for easy deployment
- **FastAPI**: Modern, fast web framework with automatic API documentation

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Simple-Backend-CICD
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t quote-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 quote-api
   ```

## 🌐 API Endpoints

### Base URL
```
http://localhost:8000
```

### Available Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Root endpoint with API information | `{"message": "Quote API is running! Visit /quote to get a random quote."}` |
| `/quote` | GET | Get a random inspirational quote | `{"quote": "The only way to do great work is to love what you do. - Steve Jobs"}` |
| `/health` | GET | Health check endpoint | `{"status": "healthy"}` |

### Example Usage

```bash
# Get a random quote
curl http://localhost:8000/quote

# Check API health
curl http://localhost:8000/health

# Get API information
curl http://localhost:8000/
```

## 📚 API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 Configuration

### CORS Settings
The API is configured to allow requests from common frontend development ports:
- `http://localhost:5173` (Vite default)
- `http://localhost:3000` (Create React App default)

### Environment Variables
Currently, the application uses default settings. You can extend it by adding environment variables for:
- Database connections
- API keys
- Logging configuration
- Port configuration

## 🐳 Docker

### Build Image
```bash
docker build -t quote-api .
```

### Run Container
```bash
docker run -p 8000:8000 quote-api
```

### Docker Compose (Optional)
Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'
services:
  quote-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PORT=8000
```

## 🧪 Testing

To test the API endpoints:

```bash
# Test root endpoint
curl http://localhost:8000/

# Test quote endpoint
curl http://localhost:8000/quote

# Test health endpoint
curl http://localhost:8000/health
```

## 📦 Project Structure

```
Simple-Backend-CICD/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── venv/               # Virtual environment (not in repo)
```

## 🔄 CI/CD Integration

This project is designed to be easily integrated into CI/CD pipelines. Common integration points:

- **GitHub Actions**: Automated testing and deployment
- **Docker Hub**: Container registry for deployment
- **Kubernetes**: Container orchestration
- **Cloud Platforms**: AWS, Azure, GCP deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the API documentation at http://localhost:8000/docs
2. Review the logs for error messages
3. Open an issue in the repository

## 🔮 Future Enhancements

- [ ] Database integration for dynamic quotes
- [ ] User authentication
- [ ] Rate limiting
- [ ] Logging and monitoring
- [ ] Unit and integration tests
- [ ] Environment-specific configurations 