import asyncio
import websockets

async def connect():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        username = input("Enter your username: ")

        async def send_message():
            while True:
                message = input("Enter message: ")
                full_message = f"{username}: {message}"  # Định dạng message với username
                await websocket.send(full_message)

        async def receive_message():
            while True:
                response = await websocket.recv()
                print(f"Nhận từ server: {response}")

        # Chạy song song việc gửi và nhận message
        await asyncio.gather(send_message(), receive_message())

# Run events loop
asyncio.run(connect())
