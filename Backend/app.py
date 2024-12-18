from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
# Load your locally saved LLM
MODEL_PATH = "../ML/Model/Base/M2M100"  # Update with your model's path
tokenizer = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)


app = Flask(
    __name__,
    template_folder='../Frontend/Templates',
    static_folder='../Frontend/static'
)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Parse the incoming JSON request
    data = request.get_json()
    source_text = data['source_text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']

    # Add translation prefix (e.g., "translate {source_lang} to {target_lang}: ")
    prompt = f"translate {source_lang} to {target_lang}: {source_text}"

    # Tokenize input
    input_ids = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids

    # Generate translation
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)

    # Decode the output
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return the translation as JSON
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    # Load your locally saved LLM
    MODEL_PATH = "../ML/Model/Base/M2M100/"  # Update with your model's path
    tokenizer = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

    app.run(debug=True)
