
import json
from model import OpenAIModel
from config import YamlConfig
from chains import OneCallChain

"""
助手类，负责接收输入，调用链，返回输出。
后续可以保存聊天记录、链路由等
"""
class Assistant:
    def __init__(self, system_message: str="你是一个通用的生活助理，能回答所有生活中的问题") -> None:
        config = YamlConfig()
        api_key = config.__getattr__("model")["openai_api_key"]
        model = OpenAIModel(model_name="gpt-3.5-turbo",api_key=api_key)
        self.one_call_chain = OneCallChain(llm = model.create_chat_model(),system_message=system_message)

    def ask(self, question: str, history):
        print(history)
        return self.one_call_chain.run(question)