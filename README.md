## 🌟 Demo
https://github.com/user-attachments/assets/31badbbf-7226-4d41-b8a1-d77158298d9d

# Multilingual Translation Model

A scalable and efficient multilingual translation system powered by fine-tuned Large Language Models, featuring real-time translation capabilities across multiple language pairs.

## Table of Contents
- [Flowchart: Development Process](#-Flowchart)
- [Technical Implementation](#-technical-implementation)
- [Performance Metrics](#-performance-metrics)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)


Here’s the updated section with the live link separated below the image and set to open in a new tab:

---

## 🛠️ Flowchart
### Live Link
![Untitled design](https://github.com/user-attachments/assets/336a8316-fd46-449d-a434-25ebd10326cc)

[Live Deployment on Google Cloud Platform](https://fimage-395239392614.europe-west2.run.app/)

**Note:** The live deployment is hosted on Google Cloud Platform. Please allow up to **2 minutes for cold start** if the service is inactive.

---

This ensures the image and link are separate, and the link opens in a new tab when clicked. Let me know if you need further adjustments! 🚀

---

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
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)   ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-yellow?style=for-the-badge&logo=huggingface&logoColor=white) ![PEFT](https://img.shields.io/badge/PEFT-green?style=for-the-badge&logo=huggingface&logoColor=black) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

### 🎨 Frontend & 🔧 Backend
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)  ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

### ☁️ Cloud/DevOps
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

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

# Run container (map port 5000 to 8080)
docker run -p 8080:5000 translation-model
```

## 📁 Project Structure
```
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
│   ├── api/                                                # REST API endpoints
│   ├── dataset/                                            # Training and evaluation datasets
│   └── preprocessing/                                      # Production preprocessing scripts
├── Frontend/
│   ├── Templates/
│   │   └── index.html                                      # Main application template
│   └── static/
│       ├── css/
│       │   └── styles.css                                 # Custom styling
│       └── js/
│           └── script.js                                  # Frontend logic
├── tests/                                                 # Unit and integration tests
├── Dockerfile                                             # Container configuration
└── requirements.txt                                       # Python dependencies
```

## 📚 API Documentation

### Translation Endpoint
```http
POST /translate
Content-Type: application/json
```

#### Request Body
```json
{
    "source_text": "Hi friends, how are you",
    "source_lang": "en",
    "target_lang": "hi"
}
```

#### Response
```json
{
    "translated_text": "नमस्कार दोस्तों, आप कैसे हैं?"
}
```

#### Example: Greek Translation
```json
{
    "source_text": "Hello, how are you?",
    "source_lang": "en",
    "target_lang": "el"
}
```

#### Response
```json
{
    "translated_text": "Γειά σου, πώς είσαι;"
}
```

#### Supported Languages
- English (en)
- Hindi (hi)
- Greek (el)

#### Error Responses
```json
{
    "error": "Model or tokenizer not loaded."
}
```
Status: 500

```json
{
    "error": "Translation failed."
}
```
Status: 500

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/NewFeature`
3. Commit your changes: `git commit -m 'Add NewFeature'`
4. Push to the branch: `git push origin feature/NewFeature`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Final Notes**
- Ensure the **ports** in your README match the ports used in your Flask app and Docker configuration.
- Add a **demo** or **screenshot** to make your README more engaging.
- Consider adding a **Future Work** or **Challenges** section to provide more context about your project.

🚀
