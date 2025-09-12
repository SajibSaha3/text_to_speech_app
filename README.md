
  <h1>🗣️ Bangla & English Text-to-Speech (Streamlit App)</h1>
  <p>
    This project is a <strong>Text-to-Speech (TTS) application</strong> built with <strong>Streamlit</strong>, 
    supporting both <strong>manual text input</strong> and <strong>PDF text extraction</strong>.  
    It provides two speech synthesis options: <strong>gTTS (Google Text-to-Speech, online)</strong> 
    and <strong>pyttsx3 (offline, English only)</strong>.
  </p>

  <h2>🚀 Features</h2>
  <ul>
    <li>✅ Convert <strong>Bangla & English text</strong> to speech</li>
    <li>✅ Two input modes:
      <ul>
        <li>Manual text entry</li>
        <li>Upload PDF and select a page</li>
      </ul>
    </li>
    <li>✅ Dual TTS Engines:
      <ul>
        <li><strong>gTTS (online)</strong> → Supports Bangla & English</li>
        <li><strong>pyttsx3 (offline)</strong> → English only</li>
      </ul>
    </li>
    <li>✅ Audio playback inside Streamlit UI</li>
    <li>✅ Error handling for invalid inputs and missing text</li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li>Streamlit – Web UI framework</li>
    <li>PyPDF2 – PDF text extraction</li>
    <li>gTTS – Google Text-to-Speech (online)</li>
    <li>pyttsx3 – Offline TTS engine (English only)</li>
    <li>tempfile / os – Temporary file handling</li>
  </ul>

  <h2>📦 Installation</h2>
  <ol>
    <li>Clone the repository</li>
    <li>Create and activate a virtual environment</li>
    <li>Install required dependencies from <code>requirements.txt</code></li>
    <li>Run the app using Streamlit</li>
  </ol>

  <h2>▶️ Usage</h2>
  <div class="highlight">
    streamlit run app.py
  </div>
  <p>This will open the TTS app in your browser.</p>

  <h2>📖 How It Works</h2>
  <h3>1. Input Options</h3>
  <ul>
    <li><strong>Manual Text Entry</strong>: Enter text directly in the text box</li>
    <li><strong>PDF Upload</strong>: Upload a PDF file → Select a page → Extract text → Preview it</li>
  </ul>

  <h3>2. Choose Language & Engine</h3>
  <ul>
    <li><strong>Languages</strong>: English or Bangla</li>
    <li><strong>Engines</strong>:
      <ul>
        <li>gTTS (works online, supports Bangla & English)</li>
        <li>pyttsx3 (offline, English only)</li>
      </ul>
    </li>
  </ul>

  <h3>3. Generate Speech</h3>
  <ul>
    <li>Click <strong>Convert to Speech</strong></li>
    <li>If successful, an audio player will appear with the generated file</li>
    <li>gTTS outputs <code>MP3</code> format, pyttsx3 outputs <code>WAV</code> format</li>
  </ul>

  <h2>🖼️ Demo UI</h2>
  <ul>
    <li>📄 Upload PDF → Extract text from selected page</li>
    <li>✍️ Enter text manually → Convert directly</li>
    <li>🔊 Select TTS engine → Play generated audio</li>
  </ul>

  <h2>📌 Example</h2>
  <div class="highlight">
    Input Text: Hello, আজকের দিনটা সুন্দর।<br>
    Output: 🎧 A natural voice combining English and Bangla speech (using gTTS).
  </div>

  <h2>📜 License</h2>
  <p class="license">MIT License – Free to use, modify, and distribute.</p>
