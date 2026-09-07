# OpenHands Server - Main Application
# Cyber Alpha System - CASLABBR

import os
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI(title="Cyber Alpha System", version="2.4.1")

@app.get("/")
async def root():
    return {"status": "online", "system": "Cyber Alpha", "version": "2.4.1"}

@app.get("/health")
async def health():
    return {"status": "healthy", "agents": 10}

@app.get("/conversations/{conv_id}")
async def get_conversation(conv_id: str):
    return {"id": conv_id, "status": "active"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))