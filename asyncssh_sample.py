import asyncio, asyncssh, sys

async def run_client(host, username, password):
    async with asyncssh.connect(host, username=username, password=password) as conn:
        writer, reader, errout = await conn.open_session()
        x=1
        print(x)
        backspace = '\x08'
        writer.write(backspace)
        result = await asyncio.wait_for(reader.read(4096), timeout=3)
        print(result)
        enter = '\n'
        writer.write(enter)
        writer.write(enter)
        result = await asyncio.wait_for(reader.read(4096), timeout=3)
        print(result)
        # writer.write(backspace)
        # result = await asyncio.wait_for(reader.readexactly(4096), timeout=3)
        # print(result)
        pass



# try:
host = "tty.sdf.org"
username = "jcal0"
password = "ZVTKoZ9HfPRQ"


asyncio.get_event_loop().run_until_complete(run_client(host, username, password))
# except (OSError, asyncssh.Error) as exc:
    # sys.exit('SSH connection failed: ' + str(exc))