import speech_recognition as sr
import pyttsx3
import webbrowser
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

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
    engine.save_to_file(text, "response.mp3")  # Save audio response to a file
    engine.runAndWait()

def search_google(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def ask_chatbot(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    speak("How can I help you?")
    while True:
        query = listen().lower()
        if query == "":
            continue
        elif query == "exit" or query == "quit":
            speak("Goodbye!")
            break
        else:
            # Save the question or process it further
            print("Question:", query)
            response = ask_chatbot(query)
            print("Answer:", response)
            speak(response)

if __name__ == "__main__":
    main()
