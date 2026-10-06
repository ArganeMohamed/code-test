from fastapi import FastAPI

from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService


app = FastAPI(
    title="Simple Ollama API",
    version="1.0.0",
)

chat_service = ChatService()


@app.get("/")
def root():
    return {
        "message": "FastAPI + LangChain Ollama API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = chat_service.ask(request.message)

    return ChatResponse(answer=answer)