import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import gradio as gr
from assistant import Assistant

def launch_gradio():
    assistant = Assistant(system_message="你是一个擅长数学的助手，能回答所有数学问题")
    assistant_launch = gr.ChatInterface(
        fn = assistant.ask,
        title="小助手",
        chatbot=gr.Chatbot(height=500)
    )

    assistant_launch.launch(share=True,server_name="0.0.0.0")


if __name__ == "__main__":
    
    launch_gradio()