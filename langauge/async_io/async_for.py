"""
See langauge.statements_expressions.statements.iteration_protocol

Now you ask: what happens if you declare the __next__() special method as an async def coroutine function? That will
allow it to await some kind of I/O-bound operation—and this is pretty much exactly how async for works

1. You must implement def __aiter__(). (Note: not with async def!)
2. __aiter__() must return an object that implements async def __anext__().
3. __anext__() must return a value for each iteration and raise StopAsyncIteration when finished.

async for provides the ability to retain the convenience of a simple for loop, even when iterating over data where
the iteration itself is performing I/O. The benefit is that you can process enormous amounts of data with a single
loop, because you have to deal with each chunk only in tiny batches """
import asyncio

import requests


class AsyncIterationProtocol:
    def __aiter__(self):
        self.urls = iter(['https://www.google.com/', 'https://www.bing.com/'])
        return self

    async def __anext__(self):
        try:
            url = next(self.urls)
        except StopIteration:
            raise StopAsyncIteration

        loop = asyncio.get_running_loop()
        # We can await the data, which means that other code can run on the event loop while we wait on network I/O.
        result = await loop.run_in_executor(None, requests.get, url)
        return result.status_code


async def demo_async_for():
    async for status_code in AsyncIterationProtocol():
        print(status_code)


def demo():
    asyncio.run(demo_async_for())
