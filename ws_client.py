#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
    	person = '{"color": "#FF0000"}'

    	name = json.loads(person)

    	await websocket.send(person)
    	print(f"> {name}")

    	res = await websocket.recv()

    	print(f"< {res}")

asyncio.get_event_loop().run_until_complete(hello())
