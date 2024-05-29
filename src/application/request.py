"""Module to make API call to OpenAI endpoint"""

import requests
from application import generate_prompt
from config import OpenAISettings

config = OpenAISettings()

def make_open_ai_request(ts_data):
    """Function for OpenAI call"""

    # Create headers
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }

    # Prepare data
    data = {
        "model": config.MODEL,
        "prompt": generate_prompt(ts_data),
        "max_tokens": config.MAX_TOKEN
    }

    # API call
    response = requests.post(config.URL, headers=headers, json=data, timeout=180).json()
    if 'error' in response:
        raise Exception(response['error'])
    return response.json()['choices'][0]['message']['content']
