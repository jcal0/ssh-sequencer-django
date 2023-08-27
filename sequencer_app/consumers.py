import json
import asyncio
import asyncio, asyncssh, sys

from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio, asyncssh, sys


class SSH_connection_object:
    def __init__(self, host, username, password):  
        self.host = host
        self.username = username
        self.password = password
        self.stream = ''

        # asyncio.get_event_loop().run_until_complete(self.run_client(host, username, password))
        self.conn = None
        
    async def connect(self):
        self.conn = await asyncssh.connect(self.host, username=self.username, password=self.password)
        self.writer, self.reader, self.errout = await self.conn.open_session()

    async def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            
            
    async def send_command(self, command):
        self.writer.write(command + '\n')
        
    async def task1(self):
        stream = ''
        x=1
        print(x)
        backspace = '\x08'
        self.writer.write(backspace)
        await asyncio.sleep(1)
        # result = await asyncio.wait_for(self.reader.read(4096), timeout=3)
        # print(result)
        # stream += result
        enter = '\n'
        self.writer.write(enter)
        self.writer.write(enter)
        await asyncio.sleep(1)
        # result = await asyncio.wait_for(self.reader.read(4096), timeout=3)
        # print(result)
        await asyncio.sleep(1)
        # stream += result
            
        return stream
            # writer.write(backspace)
            # result = await asyncio.wait_for(reader.readexactly(4096), timeout=3)
            # self.stream += result
            
        
    #     print(stream)
    #     return stream
        
        
    # async def run_client(self):
    #     stream = ''
    #     async with asyncssh.connect(self.host, username=self.username, password=self.password) as conn:

    #         writer, reader, errout = await conn.open_session()
    #         x=1
    #         print(x)
    #         backspace = '\x08'
    #         writer.write(backspace)
    #         await asyncio.sleep(1)
    #         result = await asyncio.wait_for(reader.read(4096), timeout=3)
    #         # print(result)
    #         stream += result
    #         enter = '\n'
    #         writer.write(enter)
    #         writer.write(enter)
    #         await asyncio.sleep(1)
    #         result = await asyncio.wait_for(reader.read(4096), timeout=3)
    #         # print(result)
    #         await asyncio.sleep(1)
    #         stream += result
            
    #         # writer.write(backspace)
    #         # result = await asyncio.wait_for(reader.readexactly(4096), timeout=3)
    #         # self.stream += result
            
        
    #     print(stream)
    #     return stream
        
        



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

    async def loopnum(self, number):
        for i in range(number):
            print(i)
            await asyncio.sleep(1)
            await self.send(text_data=json.dumps({
                'message': i,
            }))
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data.get('event', '')
        message = data.get('message', '')
        number = data.get('number', '')
        msg_type = data.get('msg_type', '')
        if message == 'ping':
            await self.send(text_data=json.dumps({
                'type': 'pong',
                'listdata': 'Pong! You sent a ping.'
            }))
        
        
        if event == 'connect_ssh':
            host = data.get('host', '')
            username = data.get('username', '')
            password = data.get('password', '')
            self.ssh_conn_instance = SSH_connection_object(host, username, password)
            await self.ssh_conn_instance.connect()
            asyncio.create_task(self.ssh_conn_instance.task1())
            self.keep_reading_task = asyncio.create_task(self.keep_reading())
            
            
        if event == 'command':
            input = data.get('input', '')
            await self.ssh_conn_instance.send_command(input)

        
        if message == 'infinite':
            await self.send(text_data=json.dumps({
                'num': number,
                'listdata': 'Pong! You sent a ping.'
            }))
            asyncio.create_task(self.loopnum(number))

        if message == 'connect':
            
            host = "tty.sdf.org"
            username = "jcal0"
            password = "ZVTKoZ9HfPRQ"

            self.ssh_conn_instance = SSH_connection_object(host, username, password)
            await self.ssh_conn_instance.connect()
            # task1_output = await self.ssh_conn_instance.task1()
            
            
            asyncio.create_task(self.ssh_conn_instance.task1())
            # await self.send(text_data=json.dumps({
            #     'type':'term',
            #     'message':task1_output
            # }))
            
            self.keep_reading_task = asyncio.create_task(self.keep_reading())
            print('Sleeping for 10')
            # await asyncio.sleep(180)
            # await self.ssh_conn_instance.disconnect()
            # print('done')

        if msg_type == 'term':
            await self.ssh_conn_instance.send_command(message)
            
            
    async def keep_reading(self):
        while True:
            if self.ssh_conn_instance.conn is not None:
                result = await self.ssh_conn_instance.reader.read(4096)
                if result:
                    await self.send(text_data=json.dumps({
                        'type':'term',
                        'message':result
                    }))
                await asyncio.sleep(0.2)
                # result = await asyncio.wait_for(self.ssh_conn_instance.reader.read(4096), timeout=3)
        pass

    async def disconnect(self, close_code):
        await self.ssh_conn_instance.disconnect()