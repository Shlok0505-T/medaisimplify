from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class SimplifyRequest(BaseModel):
    input_value: str
    output_type: str = "chat"
    input_type: str = "chat"

@app.post("/api/simplify")
def simplify_text(payload: SimplifyRequest):
    try:
        api_url = os.getenv("API_URL", "http://localhost:7860/api/v1/run/1effbd4f-0774-486b-971c-6431bf605188")
        api_key = os.getenv("API_KEY", "sk-KoHDHZh68T9juZavQoTOgjDGx1Nn68TeWqe6AfEACvg")
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }
        response = requests.post(
            f"{api_url}?stream=false",
            headers=headers,
            json=payload.dict()
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}