import speech_recognition as sr
import pyttsx3
import webbrowser

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I encountered an error.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def search_google(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    speak("How can I help you?")
    while True:
        query = listen().lower()
        if query == "":
            continue
        elif query == "exit" or query == "quit":
            speak("Goodbye!")
            break
        elif query == "what is your name":
            speak("My name is chiitii i am a google asistant made by JG.")
        elif query == "how are you?":
            speak("I'm doing well, thank you!")
        elif query == "open website":
            speak("Sure, which website would you like to open?")
            website = listen().lower()
            search_google(website)
        # Add more question-action pairs here
        else:
            # Default response for unrecognized questions
            speak("I'm sorry, I don't have an answer for that.")

if __name__ == "__main__":
    main()