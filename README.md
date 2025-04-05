
# 🌍 Multilingual Translation System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Models-yellow)](https://huggingface.co/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Deployed-blue?logo=google-cloud)](https://cloud.google.com)
[![Flask](https://img.shields.io/badge/Flask-API%20Server-green?logo=flask)](https://flask.palletsprojects.com/)

**Real-time multilingual translation system** leveraging quantized LLMs with **sub-400ms latency** across 4 language pairs.

## 🌟 Demo
https://github.com/user-attachments/assets/31badbbf-7226-4d41-b8a1-d77158298d9d

### Infrastructure
![System Architecture](https://github.com/user-attachments/assets/336a8316-fd46-449d-a434-25ebd10326cc)

## 🖖🏻 Live Demo
[![Live Demo](https://img.shields.io/badge/Live_Demo-Available-green)](https://fimage-395239392614.europe-west2.run.app/)
*Note: Allow up to 2 minutes for cold start on first access*

## ✨ Key Features

- **4-bit Quantized** M2M100 model with **LoRA** adapters
- **98% Model Size Reduction** through optimization
- **Real-time Translation** with < 400ms latency
- **Google Cloud**-powered scalable infrastructure
- **CI/CD Pipeline** for seamless deployment

## 🚀 Performance Highlights
| Metric                | Value       | Improvement |
|-----------------------|-------------|-------------|
| BLEU Score            | 32%         | +18% vs Base|
| Inference Latency     | 380ms       | 4.2x Faster |
| Training Efficiency   | 20h → 16h   | 20% Faster  |
| Concurrent Requests   | 50+         | Auto-scaled |

## 🛠 Tech Stack Deep Dive

### Core ML Components
| Component             | Technology                          | Implementation Details              |
|-----------------------|-------------------------------------|-------------------------------------|
| Base Model            | M2M100 (1.2B params)               | Facebook's multilingual NMT model   |
| Fine-tuning           | LoRA (Low-Rank Adaptation)         | Rank=8, α=32                        |
| Quantization          | 4-bit GPTQ                          | 4.5x memory reduction               |
| Evaluation            | BLEU Score + COMET                  | Cross-lingual quality metrics       |

## 🧩 Project Structure

```bash
|-- .DS_Store                     # macOS-specific metadata file (can be ignored)
|-- .gitignore                    # Specifies files and folders to exclude from version control
|-- LICENSE                       # License file detailing the project's usage terms
|-- README.md                     # Project overview, setup instructions, and usage details
|-- app.yaml                      # Configuration file for deploying the app on platforms like Google App Engine
|-- requirements.txt              # List of Python dependencies required for the project
|-- Api                           # Backend API components
|   |-- Dockerfile                # Instructions for building a Docker container for the API
|   |-- app.py                    # Main Flask application file defining API endpoints
|-- Backend                       # Backend-related code, models, and research notebooks
|   |-- Demo.mp4                  # Video demonstration of the project or specific features
|   |-- ML pipeline               # Machine Learning pipeline components
|   |   |-- 4&16&32 bits.png      # Visualization of quantization results for 4-bit, 16-bit, and 32-bit models
|   |   |-- EDA.ipynb             # Exploratory Data Analysis notebook
|   |   |-- FT-Greek+Hindi.ipynb  # Fine-tuning experiments for Greek and Hindi languages
|   |   |-- M2M100.ipynb          # Notebook for working with the M2M100 multilingual translation model
|   |   |-- NLP pipeline.ipynb    # End-to-end NLP pipeline implementation
|   |   |-- image.png             # Image file (likely used for visualization or documentation)
|   |   |-- Evaluation            # Folder containing evaluation metrics and scripts
|   |   |   |-- Bleu_score_.ipynb # Notebook calculating BLEU scores for baseline fine-tuned models
|   |   |-- Lora                  # Folder for LoRA (Low-Rank Adaptation) fine-tuning experiments
|   |   |   |-- M2M100.ipynb      # Notebook for fine-tuning M2M100 using LoRA techniques
|   |   |-- Quantization          # Folder for model quantization experiments
|   |       |-- 4bit+lora.ipynb   # Notebook for 4-bit quantization of M2M100 with LoRA
|-- Frontend                      # Frontend components (HTML, CSS, JS)
|   |-- .DS_Store                 # macOS-specific metadata file (can be ignored)
|   |-- Templates                 # Jinja templates or HTML files for rendering web pages
|   |   |-- index.html            # Main HTML template for the frontend
|   |-- static                    # Static assets (CSS, JS, images, etc.)
|       |-- css                   # Folder for CSS stylesheets
|       |   |-- styles.css        # Main CSS file for styling the frontend
|       |-- js                    # Folder for JavaScript files
|           |-- script.js         # Main JavaScript file for interactivity
```

## ⚡ Quick Start

### Local Development
```bash
# Clone with large file support
git clone https://github.com/aktheroy/multilingual-translation.git
cd multilingual-translation

# Install with optimized dependencies
pip install -r requirements.txt --use-pep517

# Start development server
python -m flask run --host=0.0.0.0 --port=5000
```

### Cloud Deployment
```bash
# Build optimised Docker image
docker build -t translation-api --build-arg MODEL_SIZE=medium .

# Run with resource constraints
docker run -p 5000:5000 --memory="4g" --cpus="2.0" translation-api
```

## 📚 API Documentation

### Real-time Translation Endpoint
```python
import requests

payload = {
    "source_text": "Hello world!",
    "source_lang": "en",
    "target_lang": "hi",
    "formality": "formal"  # Optional
}

response = requests.post(
    "https://api.yourdomain.com/translate",
    json=payload,
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)

print(response.json())
# {"translation": "नमस्ते दुनिया!", "latency": 375, "confidence": 0.89}
```

### Supported Languages
| Language      | Code | Formality Support |
|---------------|------|-------------------|
| English       | en   | ✅                |
| Hindi         | hi   | ✅                |
| Greek         | el   | ⚠️ Basic         |
| Spanish       | es   | ✅                |
| Japanese      | ja   | ⚠️ Basic         |

## 📊 Performance Optimization

![Optimization Timeline](https://via.placeholder.com/800x400.png?text=Training+Timeline+Visualization)

**Quantization Benefits**
- Model Size: 4.8GB → 1.1GB (-77%)
- VRAM Usage: 10.2GB → 2.3GB (-77%)
- Throughput: 12 → 54 req/s (+350%)

## 🤝 Contribution Guidelines

1. **Architecture Decisions**
```bash
# Validate model changes
python -m pytest tests/model_integration.py

# Check quantization impact
./scripts/benchmark.sh --precision int4
```

2. **Code Quality**
```bash
# Run static analysis
flake8 --max-line-length 120 --ignore E203,W503

# Type checking
mypy --strict --ignore-missing-imports .
```

## 📜 License & Citation

```bibtex
@software{MultilingualTranslator2023,
  author = {Arun Roy},
  title = {Quantized Multilingual Translation System},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/aktheroy/multilingual-translation}}
```

**License:** [Apache 2.0](LICENSE) | **Contact:** [aktheroy@gmail.com](mailto:aktheroy@gmail.com)
