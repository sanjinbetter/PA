from langchain_openai import ChatOpenAI
from model import BaseModel

class OpenAIModel(BaseModel):

    def __init__(self, model_name: str = "gpt-3.5-turbo", api_key: str = None, verbose: bool = True) -> None:
        self.model_name = model_name
        self.api_key = api_key
        self.verbose = verbose


    def create_chat_model(self, model_name: str, verbose: bool = True):

        return ChatOpenAI(
            model_name = model_name if model_name is not None else self.model_name,
            api_key=self.api_key,
            verbose=verbose if verbose is not None else self.verbose,
        )