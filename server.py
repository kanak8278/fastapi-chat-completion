from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Initialize the FastAPI app
app = FastAPI()

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("kanak8278/gemma-2b-oasst2-01")
model = AutoModelForCausalLM.from_pretrained("kanak8278/gemma-2b-oasst2-01")

# Define request and response schemas
class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]

class ChatCompletionResponse(BaseModel):
    role: str
    content: str

# Define the chat completion endpoint
@app.post("/chat/completions", response_model=List[ChatCompletionResponse])
async def create_chat_completion(request: ChatCompletionRequest):
    if request.model != "gemma-2b-oasst2-01":
        raise HTTPException(status_code=400, detail="Model not supported")

    # Concatenate messages to form the input
    input_text = ""
    for message in request.messages:
        input_text += f"{message.role}: {message.content}\n"
    
    # Tokenize the input
    input_ids = tokenizer(input_text, return_tensors="pt")

    # Generate the model's response
    outputs = model.generate(**input_ids, max_new_tokens=100)
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Create the response
    response = [ChatCompletionResponse(role="gpt", content=output_text)]

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
