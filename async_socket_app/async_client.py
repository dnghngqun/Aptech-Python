import asyncio

# tcp: transition control protocol
async def tcp_client(message):
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888
    )
    print(f"Client: {message}")
    writer.write(message.encode())
    
    # đợi phản hồi từ server
    data = await reader.read(100)
    print(f"Nhận: {data.decode()}")
    print("Đóng kết nối")
    writer.close()
    await writer.wait_closed()
    
async def main(): #chạy nheièu client bất đồng bộ
    messages = ['Client 1: Xin chao', 'Client 2: Hello', 'Client 3: Bonjour', 'Client 4: Hola', 'Client 5: Ciao']
    tasks = [tcp_client(mess) for mess in messages]
    await asyncio.gather(*tasks)
    
#event loop
asyncio.run(main())
    