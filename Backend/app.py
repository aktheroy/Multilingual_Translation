from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load your locally saved LLM
MODEL_PATH = "/ML/Model/Base/M2M100"  # Update with your model's path
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)  # Load the tokenizer globally
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)  # Load the model globally

# Initialize Flask app
app = Flask(
    __name__,
    template_folder='../Frontend/Templates',
    static_folder='../Frontend/static'
)

@app.route('/')
def index():
    """Serve the homepage."""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """Handle translation requests."""
    # Parse the incoming JSON request
    data = request.get_json()

    # Extract fields from the JSON payload
    source_text = data.get('source_text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')

    # Check for missing required parameters
    if not source_text or not source_lang or not target_lang:
        return jsonify({'error': 'Missing required parameters'}), 400

    # Create translation prompt
    prompt = f"translate {source_lang} to {target_lang}: {source_text}"

    try:
        # Tokenize the input
        input_ids = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids

        # Generate the translation
        with torch.no_grad():
            outputs = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)

        # Decode the generated tokens into text
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Return the translated text as a JSON response
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
