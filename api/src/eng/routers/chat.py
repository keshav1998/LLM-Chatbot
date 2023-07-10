from fastapi import APIRouter
from langchain import PromptTemplate, LLMChain
from langchain.schema import SystemMessage, messages_to_dict, AIMessage, HumanMessage
from src.eng.models.model import model_loader
from pydantic import BaseModel
import logging
from src.eng.models.chat import Chat

logging.basicConfig(level=logging.INFO)

chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@chat_router.get("/")
async def read_root():
    return {"Welcome": "To LLM API house"}

@chat_router.post("/")  # type: ignore          
async def infer(question: Chat):
    '''
    question: user input text
    return: response from LLM API
    '''
    # Get prompt from API call
    llm, prompt = model_loader()
    question = question.question
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Generate response
    answer = llm_chain.run(question=question)

    if not isinstance(answer, str):
        answer = str(answer)

    ai_message = AIMessage(content=answer)
    return ai_message