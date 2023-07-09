# Create a simple gradio ui like chat gpt that interacts with LLM API

import gradio as gr
import requests
import json

def get_response(input_text):
    url = "http://" + "127.0.0.1" + ":" + "9098" + "/api/api/chat/"
    payload = json.dumps({"question": input_text, "description":''})  # convert dict to json string
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["content"]

iface = gr.Interface(fn=get_response, inputs="textbox", outputs="textbox")
iface.launch(share=True)

# Run the app
# python app.py

