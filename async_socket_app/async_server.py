import asyncio

async def handle_client(reader, writer):
    #read data from client
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    
    print(f"Nhận {message} từ {addr}")
    
    #response to client
    response = f"Server: {message}"
    writer.write(response.encode())
    await writer.drain() #đảm bảo gửi hết dữ liệu trước khi tiếp tục
    
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client,
        '127.0.0.1',
        8888
        )
    addr = server.sockets[0].getsockname()
    
    print(f"Server started at {addr}")
    async with server:
        await server.serve_forever()
    
asyncio.run(main()) #Chạy even loop