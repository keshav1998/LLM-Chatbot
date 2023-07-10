from langchain import HuggingFaceHub, PromptTemplate
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)


env_file = ".env"
if os.path.exists(env_file):
    load_dotenv(env_file)
    logging.info(f'Loading environment variables from {env_file}...')


MIN_TRANSFORMERS_VERSION = '4.25.1'

# check transformers version
assert transformers.__version__ >= MIN_TRANSFORMERS_VERSION, f'Please upgrade transformers to version {MIN_TRANSFORMERS_VERSION} or higher.'


def model_loader():
    '''
    Load model from HuggingFace Hub, pass it to LLMChain, and return LLMChain object

    return: LLMChain object
    
    '''
    repo_id = os.getenv("REPO_ID")
    try:
        llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 128}, 
                             huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
        template = """Question: {question}

        Answer: The answer to this question is:"""

        prompt = PromptTemplate(template=template, input_variables=["question"])
        return llm, prompt
    except Exception as e:
        logging.error(f'Connection interrupted for download, retry model download {e}')
