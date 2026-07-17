"""
llm.py

Handles all communication with the LLM.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    API_KEY = st.secrets.get("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openai/gpt-4.1-mini"

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def call_llm(prompt, system_prompt="You are a helpful AI assistant."):
    """
    Sends a prompt to the LLM and returns the response.

    Args:
        prompt (str): User prompt.
        system_prompt (str): System instruction.

    Returns:
        str: AI response.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=2000
    )

    return response.choices[0].message.content