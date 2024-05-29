from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from model import BaseModel
from langchain_core.output_parsers import StrOutputParser

from util import LOG

"""
基础聊天链
"""
class OneCallChain:
    def __init__(self, llm, system_message: str = "你是一个通用的生活助理，能回答所有生活中的问题"):
        system_prompt = SystemMessagePromptTemplate.from_template(system_message)
        human_prompt = HumanMessagePromptTemplate.from_template("请回答问题: {question}")

        chat_prompt = ChatPromptTemplate.from_messages([system_prompt,human_prompt])

        output_parser = StrOutputParser()

        self.chain = chat_prompt | llm | output_parser

    def run(self, text: str):
        return self.chain.invoke({"question":text})