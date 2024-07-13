import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "sample-explorer"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()


def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )


st.title("Gemini Explorer")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if st.session_state.user_name == "":
    with st.form(key="user_form"):
        user_name = st.text_input("Please enter your name:")
        submit_button = st.form_submit_button(label="Submit")
        if submit_button and user_name:
            st.session_state.user_name = user_name

if st.session_state.user_name:
    for index, message in enumerate(st.session_state.messages):
        content = Content(
            role=message["role"],
            parts=[Part.from_text(message["content"])]
        )

        if index != 0:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        chat.history.append(content)

    if len(st.session_state.messages) == 0:
        initial_prompt = f"Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive and singing speak. Incorporate the user's name: {st.session_state.user_name}"
        llm_function(chat, initial_prompt)

    query = st.chat_input("Gemini Explorer")

    if query:
        with st.chat_message("user"):
            st.markdown(query)
        llm_function(chat, query)
