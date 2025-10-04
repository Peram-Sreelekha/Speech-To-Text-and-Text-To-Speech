# Speech-To-Text-and-Text-To-Speech
Convert text to speech with gTTS and speech to text from .wav files with PocketSphinx (offline). A simple Python project for learning voice apps, offline transcription, or building voice assistants.Generate audio from text or transcribe .wav files — perfect for voice apps and assistants.

This project demonstrates end-to-end speech processing using Python:
Text-to-Speech (TTS): Speak your text using gTTS and save it as an MP3 file.
Speech-to-Text (STT): Transcribe audio (.wav) files offline with PocketSphinx.
Perfect for experimenting with voice assistants, offline transcription, or just having fun with speech technologies!

#  Installation
Make sure Python 3.7+ is installed, then run:
pip install gTTS SpeechRecognition pocketsphinx

# Text-to-Speech:
text_to_speech("Hello Everyone! Have a great day!", "tts_output.mp3")
Generates an MP3 file and tries to play it automatically.

# Speech-to-Text:
speech_to_text("your_audio_file.wav")
Transcribes your .wav file to text using PocketSphinx.
⚠️ You need to provide your own audio files; none are included.
# Add support for other audio formats (MP3, OGG).






