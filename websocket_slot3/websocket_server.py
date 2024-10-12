from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases
import asyncio

DATABASE_URL = "sqlite:///./chat.db"
database = databases.Database(DATABASE_URL)

# Cấu hình SQLAlchemy để lưu vào lịch sử chát vào SQLite
metadata = MetaData()
Base = declarative_base()

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    message = Column(String, index=True)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

clients = []

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def get():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>WebSocket Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>
            <input type="text" id="username" placeholder="Enter your name" />
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off" placeholder="Enter message"/>
                <button>Send</button>
            </form>
            <ul id='messages'>
            </ul>
            <script>
                var ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages');
                    var message = document.createElement('li');
                    message.textContent = event.data;
                    messages.appendChild(message);
                };
                function sendMessage(event) {
                    var input = document.getElementById("messageText");
                    var username = document.getElementById("username").value || "Anonymous";
                    ws.send(username + ": " + input.value);
                    input.value = '';
                    event.preventDefault();
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    await send_chat_history(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            username, message = data.split(": ", 1)
            await save_message(username, message)
            await broadcast_message(data)
    except WebSocketDisconnect:
        clients.remove(websocket)
        await broadcast_message("A client disconnected.")
    finally:
        if websocket in clients:
            clients.remove(websocket)
        await websocket.close()

async def broadcast_message(message: str):
    for client in clients:
        await client.send_text(message)

async def save_message(username: str, message: str):
    query = ChatMessage.__table__.insert().values(username=username, message=message)
    await database.execute(query)

async def send_chat_history(websocket: WebSocket):
    query = ChatMessage.__table__.select().order_by(ChatMessage.id)
    rows = await database.fetch_all(query)
    for row in rows:
        await websocket.send_text(f"{row['username']}: {row['message']}")
