from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# CORS for Laravel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    message: str

@app.post("/command")
async def handle_command(cmd: Command):
    # Replace this with actual AI logic connection
    print(f"Command received: {cmd.message}")
    return {"response": f"OBLIVION received: {cmd.message}"}

@app.get("/status")
async def status():
    # Mocked status - replace with real metrics
    return {"status": "running", "trades_today": 0, "balance": 0.0}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
