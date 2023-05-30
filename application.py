import speech_recognition as sr
import pyttsx3
import webbrowser
import streamlit as st
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
    # Set up Streamlit UI
    st.title("Wadia Asistant")
    st.sidebar.image("speaker.png", width=50)
    st.sidebar.image("mic.png", width=50)
    question_answer_history = []

    speak("How can I help you?")
    while True:
        query = listen().lower()
        if query == "":
            continue
        elif query == "exit" or query == "quit":
            speak("Goodbye!,have a nice day ahead")
            break
        elif query == "what is your name":

            response = "My name is jg assistant."
        elif query == "how are you?":
            response = "I'm doing well, thank you!"
        elif query=="what is landslide or tell me about landslide ":
            r="landslide is disastress"
            response=r
            speak(r)
        elif query == "open website":
            speak("Sure, which website would you like to open?")
            website = listen().lower()
            search_google(website)
            response = f"Opening website: {website}"
        else:
            # Default response for unrecognized questions
            response = "I'm sorry, I don't have an answer for that."

        question_answer_history.append((query, response))

        # Display question-answer history in Streamlit
        st.write("Question-Answer History:")
        for i, (question, answer) in enumerate(question_answer_history):
            st.write(f"Q{i+1}: {question}")
            st.write(f"A{i+1}: {answer}")

        # Display speaker and microphone icons
        st.sidebar.image("speaker.png", width=50)
        st.sidebar.image("mic.png", width=50)

        # Text-to-speech for the response
        speak(response)

if __name__ == "__main__":
    main()