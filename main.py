import streamlit as st

import openai

import time

import os

st.set_page_config(page_title="AI Chatbot", page_icon="", layout="wide")
ASSISTANT_ID='asst_z83oVKRWH4nk2JJWYIPYw4FP'
THREAD_ID='thread_Wr3jipOFdp0EyiqZfcINPvV1'

api_key = st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.errpr('OpenAI API Key was not found. Please se it in Streamlit secrets or as an')
    st.stop()
client = openai.OpenAI(api_key=api_key)

st.title("AI Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

def chatbot(assistant_id, thread_id, user_input):
    try:
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )
        run = client.beta.thereads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == 'completed':
                break
            time.sleep(1)
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        
        return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f"Error getting assistant response: {str(e)}")
        return "I'm sorry, but an error occurred while processing your request."

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything")
if prompt:
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = get_assistant_response(
            ASSISTANT_ID,
            THREAD_ID,
            prompt
        )
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.sidebar.write(f"Assistant ID: {ASSISTANT_ID}")
st.sidebar.write(f"Thread ID: {THREAD_ID}")

def home_page():
    st.title("Welcome to Venti's protfolio")
    st.image("https://ih1.redbubble.net/image.3616127863.0902/flat,750x,075,f-pad,750x1000,f8f8f8.u1.jpg")


    
def main():
    with st.sidebar:
        st.subheader('About Venti')
    sections = ['Talk to Venti', 'Home Page']
    select_section = st.sidebar.radio('choose a section',sections)
    if select_section == 'Talk to Venti':
        chatbot()
    elif select_section == 'Home Page':
        home_page()

if __name__ == '__main__':
    main()
