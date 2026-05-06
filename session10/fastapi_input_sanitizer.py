"""Session 10 exercise: FastAPI endpoint that sanitises input."""
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import html

app = FastAPI()

class QueryModel(BaseModel):
    text: str

@app.get("/sanitize")
def sanitize(q: str = Query(..., min_length=1, max_length=200)):
    safe = html.escape(q)
    return {"original": q, "sanitized": safe}

@app.post("/echo")
def echo(payload: QueryModel):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="empty text")
    return {"text": html.escape(payload.text)}

if __name__ == "__main__":
    print("Run with: uvicorn session10.fastapi_input_sanitizer:app --reload")
