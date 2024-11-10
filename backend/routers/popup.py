import sys
import os
import model
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel

model_ai = model.Model()
router = APIRouter()

class DialogQuery(BaseModel):
    prompt: str

@router.post("/prompt/{user_id}")
async def get_prompt(user_id: int, dialog_query: DialogQuery):
    prompt = dialog_query.prompt
    response = model_ai.get_full_answer("datasets", prompt, int(user_id))
    return response



