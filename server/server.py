import asyncio
import websockets
import random
import time

try:
    async def send(websocket, path):
        while True:
            randomNumber = random.randint(0, 10)
            print(randomNumber)
            await websocket.send(f"{randomNumber}")
            time.sleep(1)

    start_server = websockets.serve(send, "", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

except KeyboardInterrupt:
    print("\nSERVER: Stopped")
