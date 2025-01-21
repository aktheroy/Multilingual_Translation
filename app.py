from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,BitsAndBytesConfig

# Initialize Flask app
app = Flask(
    __name__, template_folder="Frontend/Templates",
    static_folder="Frontend/static"
)

# Load the model and tokenizer at startup
def load_model():
    try:
        # Load model and tokenizer from Hugging Face Hub
        model = AutoModelForSeq2SeqLM.from_pretrained("aktheroy/FT_Translate_en_el_hi")
        tokenizer = AutoTokenizer.from_pretrained("aktheroy/FT_Translate_en_el_hi")
        print(f"Model loaded: {model.__class__.__name__}")
        print(f"Tokenizer loaded: {tokenizer.__class__.__name__}")
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model or tokenizer: {e}")
        return None, None

# Translate text using the model
def translate_text(model, tokenizer, source_text, source_lang, target_lang):
    try:
        # Set source language and tokenize input text
        tokenizer.src_lang = source_lang
        encoded_text = tokenizer(source_text, return_tensors="pt")

        # Generate translation
        generated_tokens = model.generate(
            **encoded_text, forced_bos_token_id=tokenizer.get_lang_id(target_lang)
        )

        # Decode and return the translated text
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return translated_text[0]
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

# Load the model and tokenizer
model, tokenizer = load_model()

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for translation
@app.route("/translate", methods=["POST"])
def translate():
    # Get JSON data from the request
    data = request.get_json()
    source_text = data.get("source_text")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")

    # Check if model and tokenizer are loaded
    if not model or not tokenizer:
        return jsonify({"error": "Model or tokenizer not loaded."}), 500

    # Translate the text using the model
    translated_text = translate_text(model, tokenizer, source_text, source_lang, target_lang)

    # Check if translation was successful
    if not translated_text:
        return jsonify({"error": "Translation failed."}), 500

    # Return the translated text
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True, port=8080)