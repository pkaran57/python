"""
Support for coroutines in context managers turns out to be exceptionally convenient. This makes sense,
because many situations require network resources—say, connections—to be opened and closed within a well-defined
scope.

See langauge/exception/context_management.py

Example:

class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return conn
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

async with Connection('localhost', 9001) as conn:
    <do stuff with conn>

Above example using @contextmanager decorator:

from contextlib import asynccontextmanager

@asynccontextmanager
async def web_page(url):
    data = await download_webpage(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)

Just because you’re using asyncio in your program, that doesn’t mean that all your context managers must be async
ones like these. They’re useful only if you need to await something inside the enter and exit methods. If there is no
blocking I/O code, just use regular context managers. """


def demo():
    print('Read pydoc in the source file')
