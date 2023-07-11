# LLM Chatbot 🦙

LLM chat is a chat interface crafted with [huggingface-falcon-7B](https://huggingface.co/tiiuae/falcon-7b) for running Alpaca models. No API keys, entirely self-hosted!
This repository contains the code for a chatbot that uses a large language model (LLM) to generate text responses. The backend of the chatbot is implemented using FastAPI, and the frontend is implemented using Gradio. Langchain is used to index and retrieve text from the LLM.

- 🌐 **Gradio** frontend
- ⚙️ **FastAPI + LangChain** for the API, wrapping calls to [huggingface-falcon-7B](https://huggingface.co/tiiuae/falcon-7b) using the [python bindings](https://python.langchain.com/docs/modules/model_io/models/llms/integrations/huggingface_hub)

🎥 Demo:

[DEMO.webm](https://github.com/keshav1998/LLM-Chatbot/assets/24654578/33bfbf55-b5f7-4172-9e37-347c87b4e6ac)

🧑🏻‍💻 Notion:
[Documentation](https://ml2018.notion.site/34a9640e9fc14508ab18e48ab78dddc4?v=ac38bd932462436ab2306ffece1ee666&pvs=4)


## ⚡️ Quick start

🐙 Docker Compose:
```
docker compose -f docker-compose.yml up -d --build
```

Then, just visit http://localhost:7860/, 

## 🖥️ Windows Setup

Ensure you have Docker Desktop installed, WSL2 configured, and enough free RAM to run models. 

## 🖥️ Windows Setup

Ensure you have Docker Desktop installed, and enough free RAM to run models, as models are using huggingface hub, ram impact will be low.

## 🧠 Supported Models

We currently support the following models:

- Airoboros 🎈
  - Airoboros-7B
- Falcon 🎈
  - Falcon-7B
- Redpajama
  - togethercomputer/RedPajama-INCITE-Instruct-3B-v1

NOTE: Airboros required llama-cpp, removed for now, for using Redpajama, change REPO_ID Env variable


## ⚠️ Memory Usage

LLaMA will crash if you don't have enough available memory for the model:

| Model        | Max RAM Required |
| ------------ | ---------------- |
| Airoboros-7B | 4.5GB            |
| Redpajama-3B | 6GB              |
| Falcon-7B    | 16GB             |

## Requirement
Huggingface hub token id

### Backend
The backend of the chatbot is implemented using FastAPI. FastAPI is a modern, high-performance web framework for Python. It is easy to use and has a lot of features that make it well-suited for building chatbots.

The backend of the chatbot consists of two main components:

A router that handles incoming requests from the frontend.
A service that interacts with Langchain to index and retrieve text from the LLM.
The router is responsible for routing incoming requests to the appropriate handlers. The service is responsible for interacting with Langchain to index and retrieve text from the LLM.

### Frontend
The frontend of the chatbot is implemented using Gradio. Gradio is a Python library that makes it easy to build interactive web applications. It is easy to use and has a lot of features that make it well-suited for building chatbots.

The frontend of the chatbot consists of a single page that allows users to interact with the chatbot. The page includes a text input field where users can enter their questions, and a text area where the chatbot's responses are displayed.

### Further information
For more information, please refer to the following resources:

FastAPI documentation: https://fastapi.tiangolo.com/
Gradio documentation: https://gradio.app/
Langchain documentation: https://langchain.readthedocs.io/en/latest/
I hope this helps!
