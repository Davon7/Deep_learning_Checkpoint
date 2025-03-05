

import streamlit as st
import speech_recognition as sr
import nltk
import random
import time

# Sample chatbot responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm not sure how to respond to that.")

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Could not request results. Check your connection."

# Streamlit App
st.title("Speech-Enabled Chatbot")
user_choice = st.radio("Choose input method:", ("Text", "Speech"))

if user_choice == "Text":
    user_input = st.text_input("You:")
    if user_input:
        response = chatbot_response(user_input)
        st.write("Bot:", response)

elif user_choice == "Speech":
    if st.button("Speak"):
        speech_text = transcribe_speech()
        st.write("You:", speech_text)
        response = chatbot_response(speech_text)
        time.sleep(1)
        st.write("Bot:", response)
