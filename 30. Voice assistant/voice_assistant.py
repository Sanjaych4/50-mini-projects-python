# Day 30: Voice assistant 


import webbrowser
import speech_recognition as sr

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the service.")
        return ""

def open_website(url):
    webbrowser.open(url)

if __name__ == '__main__':
    while True:
        command = get_command()
        if "youtube" in command:
            open_website("https://www.youtube.com")
        elif "chrome" in command:
            open_website("https://www.google.com/chrome")
        elif "whatsapp" in command:
            open_website("https://web.whatsapp.com/")
        elif "instagram" in command:
            open_website("https://www.instagram.com")
        elif "exit" in command or "quit" in command:
            break
