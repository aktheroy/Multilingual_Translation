// Helper function to adjust textarea height dynamically
function adjustTextareaHeight(textarea) {
  textarea.style.height = 'auto'; // Reset height to auto to recalculate
  textarea.style.height = Math.min(textarea.scrollHeight, 300) + 'px'; // Limit height to max-height
}

// Function to enforce word limit and update word count
function enforceWordLimit(textarea, maxWords) {
  const text = textarea.value;
  const words = text.match(/\b\w+\b/g) || []; // Match whole words only
  const wordCountElement = document.getElementById('wordCount');
  const remainingWords = maxWords - words.length;

  // Update word count display
  wordCountElement.textContent = remainingWords;

  // Enforce word limit
  if (words.length > maxWords) {
    // Trim the input to the first 50 words
    const trimmedText = words.slice(0, maxWords).join(' ');
    textarea.value = trimmedText;
    wordCountElement.textContent = 0; // Update word count to 0
    alert(`You have reached the maximum limit of ${maxWords} words.`);
    adjustTextareaHeight(textarea); // Adjust height after trimming
  }
}

// Function to handle translation
function handleTranslation() {
  const sourceLang = document.getElementById('sourceLang').value;
  const targetLang = document.getElementById('targetLang').value;

  // Check if source and target languages are the same
  if (sourceLang === targetLang) {
    alert('Source language and target language cannot be the same. Please select different languages.');
    return; // Stop the function if they are the same
  }

  const sourceText = document.getElementById('sourceText').value;
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
}

// Translate Button Event Listener
document.getElementById('translateBtn').addEventListener('click', handleTranslation);

// Reset Button Event Listener
document.getElementById('resetBtn').addEventListener('click', function () {
  // Clear only the text areas
  document.getElementById('sourceText').value = '';
  document.getElementById('translatedText').value = '';

  // Reset height of the text areas
  adjustTextareaHeight(document.getElementById('sourceText'));
  adjustTextareaHeight(document.getElementById('translatedText'));

  // Reset word count display
  document.getElementById('wordCount').textContent = '80';
});

// Adjust height of the source text area dynamically and enforce word limit
document.getElementById('sourceText').addEventListener('input', function () {
  adjustTextareaHeight(this);
  enforceWordLimit(this, 80); // Enforce 50-word limit
});

// Listen for Enter key press in the source text area
document.getElementById('sourceText').addEventListener('keydown', function (event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent default behavior (e.g., new line)
    handleTranslation(); // Trigger translation
  }
});