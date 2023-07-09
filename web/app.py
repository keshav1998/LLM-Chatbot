# Create a simple gradio ui like chat gpt that interacts with LLM API

import gradio as gr
import requests
import json

def get_response(input_text):
    # url from docker bridge network
    url = "http://" + "llm-backend" + ":" + "8967" + "/api/api/chat/"
    payload = json.dumps({"question": input_text, "description":''})  # convert dict to json string
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.text == "":
        return "No response from LLM API, wait for a few seconds and try again."
    else:
        return response.json()["content"]

iface = gr.Interface(fn=get_response, inputs="textbox", outputs="textbox")
iface.launch(server_name="0.0.0.0", server_port=7860)

