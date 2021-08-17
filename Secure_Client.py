#!/usr/bin/env python
 
# WSS (WS over TLS) client example, with a self-signed certificate
 
import asyncio
import pathlib
import ssl
import websockets
 
async def hello(host_name, port_number, ssl_context):
    uri = "wss://" + host_name + ":" + port_number
    async with websockets.connect(
        uri, ssl=ssl_context
    ) as websocket:
        name = input("What's your name? ")
 
        await websocket.send(name)
        print(f"> {name}")
 
        greeting = await websocket.recv()
        print(f"< {greeting}")
 
def secure_client_start(host_name="localhost", port_number="8765", async_func=hello):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    localhost_pem = pathlib.Path(__file__).with_name("server.crt")
    ssl_context.load_verify_locations(localhost_pem)
 
    asyncio.get_event_loop().run_until_complete(async_func(host_name, port_number, ssl_context))