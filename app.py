import streamlit as st
import random

st.set_page_config(page_title="Life Hacks Chatbot 🤖")

st.title("🧠 Life Hacks Chatbot")
st.write("Ask me for a life hack about everyday problems!")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_life_hack(user_input):
    text = user_input.lower()

    categories = {
        "study": ["study", "exam", "learn", "focus", "revision"],
        "sleep": ["sleep", "tired", "insomnia", "rest"],
        "productivity": ["productive", "work", "lazy", "motivation"],
        "clean": ["clean", "mess", "dirty", "organize"],
        "health": ["health", "energy", "tired", "diet"]
    }

    hacks = {
        "study": [
            "Use active recall instead of rereading 📚",
            "Try Pomodoro: 25 min study, 5 min break",
            "Study in short bursts and test yourself often"
        ],
        "sleep": [
            "Avoid screens 1 hour before bed 😴",
            "Keep your room cool and dark",
            "Try deep breathing like 4-7-8"
        ],
        "productivity": [
            "Start with the hardest task first 💪",
            "Use a 3-task daily priority system",
            "Turn off notifications while working"
        ],
        "clean": [
            "Clean for just 5 minutes to get started",
            "Do a nightly 10-minute reset",
            "Use music to make cleaning fun 🎵"
        ],
        "health": [
            "Drink water first thing in the morning 💧",
            "Take short walks to boost energy",
            "Stretch for 5 minutes daily"
        ]
    }

    matched_categories = []

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            matched_categories.append(category)

    if matched_categories:
        category = random.choice(matched_categories)
        return random.choice(hacks[category])

    return random.choice([
        "If it takes less than 2 minutes, do it now ⏱️",
        "Write tomorrow’s to-do list tonight",
        "Keep a notebook for ideas 💡"
    ])


# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask me for a life hack...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    reply = get_life_hack(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
