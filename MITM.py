from Secure_Server import secure_server_start
from Secure_Client import secure_client_start
import asyncio
import websockets
import pathlib
input_name = None
 
def mitm_start():
    # secure_server_start("9999", server_mitm_hello)
    # secure_client_start("localhost", "9999", client_mitm_hello)
    # put these two in their own asyncio functions
    
    print("This information was intercepted by the man in the middle. Your name is: " + input_name)
 
async def server_mitm_hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
 
    greeting = f"Hello mitm_{name}!"
 
    await websocket.send(greeting)
    print(f"> {greeting}")
 
async def client_mitm_hello(host_name, port_number, ssl_context):
    uri = "wss://" + host_name + ":" + port_number
    async with websockets.connect(
        uri, ssl=ssl_context
    ) as websocket:
        name = input("What's your name? ")
        input_name = name
 
        await websocket.send(name)
        print(f"> {name}")
 
        greeting = await websocket.recv()
        print(f"< {greeting}")