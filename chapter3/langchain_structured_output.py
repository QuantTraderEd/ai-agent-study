import os

from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain.chatmodel import init_chat_model

load_dotenv()

