import sys
import os
from flask import Flask, render_template, request, jsonify
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Add the Backend directory to the Python path (if needed)
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Backend')))

# Load the model and tokenizer
def load_model():
    model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    return model, tokenizer

# Translate text using the model
def translate_text(model, tokenizer, source_text, source_lang, target_lang):
    tokenizer.src_lang = source_lang
    encoded_text = tokenizer(source_text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.get_lang_id(target_lang))
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translated_text[0]

# Initialize Flask app
app = Flask(__name__, template_folder='../Frontend/Templates', static_folder='../Frontend/static')

# Load the model and tokenizer at startup
model, tokenizer = load_model()

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    source_text = data.get('source_text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')

    # Translate the text using the model
    translated_text = translate_text(model, tokenizer, source_text, source_lang, target_lang)

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)