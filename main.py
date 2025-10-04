from gtts import gTTS
import os
import platform
import speech_recognition as sr

# ---------------------------
# Text-to-Speech
# ---------------------------
def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Saved speech to {filename}")
    
    # Play audio
    try:
        system_name = platform.system()
        if system_name == "Windows":
            os.startfile(filename)
        elif system_name == "Darwin":
            os.system(f"afplay {filename}")
        else:
            os.system(f"mpg123 {filename}")  # Linux
    except Exception as e:
        print(f"Could not play audio automatically: {e}")
        print(f"Please open {filename} manually.")

# Example TTS
text_to_speech("Hello Everyone! Have a great day.", "tts_output.mp3")


# ---------------------------
# Speech-to-Text
# ---------------------------
def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_sphinx(audio)
        if not text.strip():
            raise sr.UnknownValueError
        print("Sphinx thinks you said:", text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print(f"Sphinx error: {e}")
    except Exception as e:
        print(f"Other error: {e}")

# Example STT
speech_to_text("download (2).wav")
