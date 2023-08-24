import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        await self.send(text_data=json.dumps({
            'type': 'connection established',
            'message': 'You are now connected!'
        }))
        
        # i = 0
        # while i < 10:
        #     await self.send(text_data=json.dumps({
        #         'type': 'pong',
        #         'listdata': f'message index: {i}'
        #     }))
        #     await asyncio.sleep(0.05)
        #     i+=1

    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')
        
        if message == 'ping':
            await self.send(text_data=json.dumps({
                'type': 'pong',
                'listdata': 'Pong! You sent a ping.'
            }))
    
    async def disconnect(self, close_code):
        pass