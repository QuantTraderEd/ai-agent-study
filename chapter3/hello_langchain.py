import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("gpt-5-nano", model_provider="openai")
result = model.invoke("랭체인이 뭔가요?")
print(type(result))
print(result.content)
