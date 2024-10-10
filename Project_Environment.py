import streamlit as st

import openai

from dotenv import load_dotenv

import os

#set up OpenAI client
api_key = st.secrets.get("OPEN_API_KEY")
client = openai.OpenAI(api_key=api_key)

def create_assistant():
    try:
        assistant = client.beta.assistants.create(
            name="Venti AI",
            instructions="You are Venti from Genshin impact",
            tools=[{"type": "code_interpreter"}],
            model="gpt-4o-mini"
        )
        return assistant
    except Exception as e:
        st.error(f"Error creating assistant: {str(e)}")
        return None

def create_thread():
    try:
        thread = client.beta.threads.create()
        return thread
    except Exception as e:
        st.error(f"Error creating thread: {str(e)}")
        return None

if __name__ == '__main__':
    assistant = create_assistant()
    thread = create_thread()
    if assistant:
        st.info(f'Assostant ID {assistant.id}')
    else:
        st.error('Failde to created an assistant')
    if thread:
        st.info(f'Thread created with ID {thread.id}')
    else:
        st.error('Failed to create a thread')
