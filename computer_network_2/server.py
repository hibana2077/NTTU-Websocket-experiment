from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from datetime import datetime
import uvicorn

app = FastAPI()

chat_app_html = open("chatapp.html",encoding="utf-8").read()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat", response_class=HTMLResponse)
async def get_chat():
    return chat_app_html

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        port = websocket.client.port
        print(f"Message text was: {data} and user port is: {port}")
        await websocket.send_text(f"- {data} -- {port} -- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    uvicorn.run("server:app", port=8080, log_level="info",reload=True,host="0.0.0.0")