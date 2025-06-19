from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/api/books")
async def proxy_books():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/books")
        return response.json()

