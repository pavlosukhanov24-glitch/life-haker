import streamlit as st
import random

# Page settings
st.set_page_config(page_title="Life Hacks Chatbot 🤖")

st.title("🧠 Life Hacks Chatbot")
st.write("Ask me for a life hack about everyday problems!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate life hack responses
def get_life_hack(user_input):

    text = user_input.lower()

    hacks = {
        "study": [
            "Try the Pomodoro technique: study 25 minutes, break 5 minutes 📚",
            "Teach what you learned to someone else — it improves memory.",
            "Use active recall instead of rereading notes."
        ],
        "sleep": [
            "Avoid screens 1 hour before bed 😴",
            "Keep your room cool and dark for better sleep.",
            "Try the 4-7-8 breathing method to fall asleep faster."
        ],
        "productivity": [
            "Start your day with the hardest task first.",
            "Write a 3-task priority list every morning.",
            "Turn off notifications while working."
        ],
        "clean": [
            "Clean for 5 minutes at a time — it feels much easier.",
            "Use baking soda and vinegar for natural cleaning.",
            "Do a 10-minute nightly reset of your space."
        ]
    }

    # Match keywords
    for keyword in hacks:
        if keyword in text:
            return random.choice(hacks[keyword])

    # Default hacks
    default_hacks = [
        "Drink water first thing in the morning 💧",
        "Write tomorrow’s to-do list before going to sleep.",
        "If something takes less than 2 minutes, do it immediately.",
        "Keep a small notebook for ideas.",
        "Set timers to stay focused."
    ]

    return random.choice(default_hacks)


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
prompt = st.chat_input("Ask me for a life hack...")

if prompt:
    
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    reply = get_life_hack(prompt)

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
