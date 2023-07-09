from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain import PromptTemplate, LLMChain
from langchain.schema import SystemMessage, messages_to_dict, AIMessage, HumanMessage
from src.eng.models.model import model_loader
from pydantic import BaseModel
from src.eng.routers.chat import chat_router
import logging

logging.basicConfig(level=logging.INFO)


class Chat(BaseModel):
    question: str
    description: str | None = None

description = """
LLM chatbot answers your questions poorly using LLaMA/alpaca. 🚀
"""
origins = [
    "http://127.0.0.1",
    "http://api:9098",
    "http://127.0.0.1:9096",
    "http://127.0.0.1:9098"
]

app = FastAPI(title="LLM Bot", version="0.0.1", description=description)
api_app = FastAPI(title="persLLM API",  version="0.0.1", description=description)
api_app.include_router(chat_router)
app.include_router(chat_router)
app.mount("/api",api_app)
api_app.mount("/api", app)

@api_app.on_event("startup")
async def startup_event():
    logging.info("Starting up...")
    logging.info("Loading model...")
    return "Model loaded successfully!"


@app.get("/")
def read_root():
    return {"Welcome": "NExT AI Chatbot"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

