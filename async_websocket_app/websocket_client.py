import asyncio
import websockets

async def connect():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        async def send_message():
           while True:
               message = input("Enter message: ")
               await websocket.send(message)
        async def receive_message():
            while True:
                response = await websocket.recv() 
                print(f"Nhận từ server: {response}")
        #chạy song song việc gửi và nhận message
        await asyncio.gather(send_message(), receive_message())
    
#run events loop
asyncio.run(connect())