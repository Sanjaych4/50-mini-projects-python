# Day 24: Convert a speech to text
# `pip install SpeechRecognition` and 'pip install pyaudio' install speechrecognition and pyaudio modules before running this program
import speech_recognition as sr

# Create a Recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now...")
    # Adjust the energy threshold based on the ambient noise level
    r.adjust_for_ambient_noise(source)
    # Listen for the user's speech input
    audio = r.listen(source)

try:
    # Use the Google Speech Recognition API to recognize the audio input
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your speech input.")
except sr.RequestError as e:
    print("Sorry, an error occurred during speech recognition:", e)
