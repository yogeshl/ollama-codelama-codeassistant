import requests
import json
import gradio as gr

# https://github.com/ollama/ollama/blob/main/docs/api.md
url="http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history =[]


def create_response(prompt):
    history.append(prompt);
    final_prompt="\n".join(history)
    
    payload = {
        "model":"CodeExpert",
        "prompt":final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code==200:
        resp = response.text
        data=json.loads(resp)
        actual_response=data["response"]
        return actual_response
    else:
        print(f"Error : {response.text}")


ui_interface=gr.Interface(
    fn=create_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your question"),
    outputs="text"
)

ui_interface.launch()