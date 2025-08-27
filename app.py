import streamlit as st
import PyPDF2
from gtts import gTTS
import pyttsx3
import os
import tempfile

# ---- Functions ----

def extract_text_from_pdf(file, page_number):
    try:
        reader = PyPDF2.PdfReader(file)
        if page_number < 1 or page_number > len(reader.pages):
            return "Invalid page number."
        page = reader.pages[page_number - 1]
        return page.extract_text()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def speak_with_gtts(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"gTTS failed: {str(e)}")
        return None

def speak_with_pyttsx3(text):
    try:
        engine = pyttsx3.init()
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        engine.save_to_file(text, temp_file.name)
        engine.runAndWait()
        return temp_file.name
    except Exception as e:
        st.error(f"pyttsx3 failed: {str(e)}")
        return None

# ---- Streamlit UI ----

st.title("🗣️ Bangla & English Text-to-Speech")
st.markdown("Choose how you want to input text and convert it to audio using gTTS or pyttsx3.")

# --- Input Selection ---
input_choice = st.radio("Select input type:", ["📝 Enter text manually", "📄 Upload PDF and select page"])

# --- Language Selection ---
language = st.selectbox("🌐 Choose language", ["English", "Bangla"])
tts_engine = st.selectbox("🗣️ Choose TTS engine", ["gTTS (Online)", "pyttsx3 (Offline - English only)"])

# --- Text Input or PDF Upload ---
if input_choice == "📝 Enter text manually":
    text_input = st.text_area("✍️ Enter your text here:")
    if text_input:
        st.session_state['text_to_convert'] = text_input.strip()

elif input_choice == "📄 Upload PDF and select page":
    pdf_file = st.file_uploader("📄 Upload PDF file", type=["pdf"])
    if pdf_file:
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)
            page_number = st.number_input("Select page number", min_value=1, max_value=total_pages, value=1)

            if st.button("Extract Text"):
                raw_text = extract_text_from_pdf(pdf_file, page_number)
                cleaned_text = ' '.join(raw_text.split()) if raw_text else ""
                st.session_state['text_to_convert'] = cleaned_text
                st.success("✅ Text extracted successfully!")

        except Exception as e:
            st.error(f"Error loading PDF: {str(e)}")

# --- Display Extracted or Entered Text ---
if 'text_to_convert' in st.session_state:
    st.text_area("📄 Extracted Text", st.session_state['text_to_convert'], height=200)

# --- Convert to Speech ---
if 'text_to_convert' in st.session_state and st.button("🔊 Convert to Speech"):
    text_cleaned = st.session_state['text_to_convert'].strip()

    if len(text_cleaned) < 5:
        st.warning("⚠️ Text is too short for speech synthesis. Please enter more content.")
    else:
        audio_path = None

        if tts_engine == "gTTS (Online)":
            lang_code = "bn" if language == "Bangla" else "en"
            audio_path = speak_with_gtts(text_cleaned, lang=lang_code)

            if audio_path and os.path.exists(audio_path):
                st.success("✅ Audio generated successfully with gTTS!")
                st.audio(audio_path, format='audio/mp3')
            else:
                st.error("❌ Failed to generate audio with gTTS.")

        elif tts_engine == "pyttsx3 (Offline - English only)":
            if language != "English":
                st.error("❌ pyttsx3 only supports English. Please select gTTS for Bangla.")
            else:
                audio_path = speak_with_pyttsx3(text_cleaned)
                if audio_path and os.path.exists(audio_path):
                    st.success("✅ Audio generated successfully with pyttsx3!")
                    st.audio(audio_path, format='audio/wav')
                else:
                    st.error("❌ Failed to generate audio with pyttsx3.")
