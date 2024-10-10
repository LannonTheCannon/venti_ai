import streamlit as st

import openai

from dotenv import load_dotenv

import os

#set up OpenAI client
client = openai(api_key=os('OPEN_API_KEY'))

def create_assistant():
    try:
        assistant = client.beta.assistants.create(
            name="Venti AI",
            instructions="You are Venti from Genshin impact",
            tools=[{"type": "code_interperter"}],
            modle="gpt-4o-mini"
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
        print(f'Assostant ID {assistant.id}')
    else:
        print('Failde to created an assistant')
    if thread:
        print('Thread created with id{thread.id}')
    else:
        print('Failed to create a thread')
