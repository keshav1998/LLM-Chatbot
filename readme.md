# LLM Chatbot 🦙

LLM chat is a chat interface crafted with [huggingface-falcon-7B](https://huggingface.co/tiiuae/falcon-7b) for running Alpaca models. No API keys, entirely self-hosted!

- 🌐 **Gradio** frontend
- ⚙️ **FastAPI + LangChain** for the API, wrapping calls to [huggingface-falcon-7B](https://huggingface.co/tiiuae/falcon-7b) using the [python bindings](https://python.langchain.com/docs/modules/model_io/models/llms/integrations/huggingface_hub)

🎥 Demo:

[DEMO.webm](https://github.com/keshav1998/LLM-Chatbot/assets/24654578/33bfbf55-b5f7-4172-9e37-347c87b4e6ac)


## ⚡️ Quick start

🐙 Docker Compose:
```
docker compose -f docker-compose.yml up -d --build
```

Then, just visit http://localhost:7860/, 

## 🖥️ Windows Setup

Ensure you have Docker Desktop installed, WSL2 configured, and enough free RAM to run models. 

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


