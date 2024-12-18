// Helper function to adjust textarea height dynamically
function adjustTextareaHeight(textarea) {
  textarea.style.height = 'auto'; // Reset height to auto to recalculate
  textarea.style.height = Math.min(textarea.scrollHeight, 300) + 'px'; // Limit height to max-height
}

// Translate Button Event Listener
document.getElementById('translateBtn').addEventListener('click', function () {
  const sourceText = document.getElementById('sourceText').value;
  const sourceLang = document.getElementById('sourceLang').value;
  const targetLang = document.getElementById('targetLang').value;
  const translatedTextArea = document.getElementById('translatedText');

  fetch('/translate', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          source_text: sourceText,
          source_lang: sourceLang,
          target_lang: targetLang,
      }),
  })
  .then(response => response.json())
  .then(data => {
      translatedTextArea.value = data.translated_text; // Display translation
      adjustTextareaHeight(translatedTextArea); // Adjust height dynamically
  })
  .catch((error) => {
      console.error('Error:', error);
  });
});


// Reset Button Event Listener
document.getElementById('resetBtn').addEventListener('click', function () {
  document.getElementById('sourceText').value = '';
  document.getElementById('translatedText').value = '';
  document.getElementById('sourceLang').selectedIndex = 0;
  document.getElementById('targetLang').selectedIndex = 0;

  // Reset height of the text areas
  adjustTextareaHeight(document.getElementById('sourceText'));
  adjustTextareaHeight(document.getElementById('translatedText'));
});

// Adjust height of the source text area dynamically
document.getElementById('sourceText').addEventListener('input', function () {
  adjustTextareaHeight(this);
});