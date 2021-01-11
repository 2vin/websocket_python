#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json

async def hello(websocket, path):
    
	try:
	    req = await websocket.recv()
	    # print(req)
	    data = json.loads(req) 
	    
	    print(data["color"])

	    res = '{"status": "ok"}'
	    await websocket.send(res)

	except:
	    res = '{"status": "failed"}'
	    await websocket.send(res)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()