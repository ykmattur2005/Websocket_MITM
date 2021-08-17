#!/usr/bin/env python
 
# WSS (WS over TLS) server example, with a self-signed certificate
 
import asyncio
import pathlib
import ssl
import websockets
 
async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
 
    greeting = f"Hello {name}!"
 
    await websocket.send(greeting)
    print(f"> {greeting}")
    
def secure_server_start(port_number=8765, async_func=hello):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    localhost_key = pathlib.Path(__file__).with_name("server.key")
    localhost_crt = pathlib.Path(__file__).with_name("server.crt")
    ssl_context.load_cert_chain(localhost_crt, localhost_key)
 
    start_server = websockets.serve(
        hello, "localhost", port_number, ssl=ssl_context
    )
 
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()