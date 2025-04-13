from fastapi import FastAPI, Depends, HTTPException, status
from schemas import ChatRequest, ChatResponse
from openai_client import ask_gpt
from crud import save_conversation


app = FastAPI()

@app.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(request: ChatRequest):
    if request is None:
        raise HTTPException(status_code=400, detail='Bad Request')
    
    messages = [{'role': 'user', 'content': request.message}]
    
    try:
        response_chatgpt = await ask_gpt(messages)
        await save_conversation(request.username, request.message, response_chatgpt)
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to ask chatgpt')
    
    return ChatResponse(response=response_chatgpt)
