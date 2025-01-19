# Multilingual Translation Model

A scalable and efficient multilingual translation system powered by fine-tuned Large Language Models, featuring real-time translation capabilities across multiple language pairs.

## 🛠️ Technical Implementation

### Model Architecture
- Fine-tuned Large Language Model using LoRA (Low-Rank Adaptation)
- Quantization techniques for model optimization
- Automated validation and preprocessing pipelines

### Backend
- Flask-based REST API server
- Scikit-learn for data preprocessing and validation
- Docker containerization for consistent deployment
- CI/CD pipeline integration for automated deployment

### Frontend
- Responsive web interface
- Real-time translation updates
- Concurrent translation support

## 📊 Performance Metrics

- **Translation Accuracy**: 32% BLEU score
- **Training Efficiency**: 20% reduction in training cycle time
- **Inference Latency**: Sub-400ms response time
- **Scalability**: Handles concurrent translation requests

## 💻 Tech Stack

### 🤖 ML/Deep Learning
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-yellow?style=for-the-badge&logo=huggingface&logoColor=white)
- PEFT (Parameter Efficient Fine-Tuning)
- BitsAndBytes for quantization

### 📊 Data Processing
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![HuggingFace Datasets](https://img.shields.io/badge/🤗%20Datasets-yellow.svg?style=for-the-badge)

### 📈 Visualization
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

### 🔧 Backend
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST%20APIs-gray?style=for-the-badge)

### 🎨 Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

### ☁️ Cloud/DevOps
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🚀 Getting Started

### Prerequisites
```bash
# Clone the repository
git clone https://github.com/yourusername/multilingual-translation.git

# Install dependencies
pip install -r requirements.txt
```

### Running Locally
```bash
# Start the Flask server
python app.py

# Access the web interface
open http://localhost:5000
```

### Docker Deployment
```bash
# Build Docker image
docker build -t translation-model .

# Run container
docker run -p 5000:5000 translation-model
```

## 📁 Project Structure
```
## 📁 Project Structure
.
├── Backend/
│   ├── ml/
│   │   ├── models/                                         # Saved model files for local/production use
│   │   └── notebooks/                                      # Jupyter notebooks for experiments
│   │       ├── EDA.ipynb                                   # Exploratory Data Analysis
│   │       ├── NLP pipeline.ipynb                          # Data preprocessing pipeline
│   │       ├── M2M100.ipynb                                # Base M2M100 implementation
│   │       ├── M2M100(Lora).ipynb                          # LoRA fine-tuning
│   │       ├── 4bit FB(M2M100)+lora.ipynb                  # 4-bit quantization
│   │       ├── 4bit FB(M2m100)+lora+Greek+Hindi.ipynb      # Multi-language support
│   │       └── Bleu_score_BFT.ipynb                        # Performance evaluation
│   ├── api/                     # REST API endpoints
│   ├── dataset/                 # Training and evaluation datasets
│   └── preprocessing/           # Production preprocessing scripts
├── Frontend/
│   ├── Templates/
│   │   └── index.html         # Main application template
│   └── static/
│       ├── css/
│       │   └── styles.css     # Custom styling
│       └── js/
│           └── script.js      # Frontend logic
├── tests/                     # Unit and integration tests
├── Dockerfile                 # Container configuration
└── requirements.txt           # Python dependencies

```

## 📋 API Documentation

### Translation Endpoint
```http
POST /api/translate
Content-Type: application/json

{
    "text": "Hello, world!",
    "source_lang": "en",
    "target_lang": "fr"
}
```

### Response
```json
{
    "translation": "Bonjour, le monde!",
    "confidence": 0.92
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/NewFeature`
3. Commit your changes: `git commit -m 'Add NewFeature'`
4. Push to the branch: `git push origin feature/NewFeature`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
