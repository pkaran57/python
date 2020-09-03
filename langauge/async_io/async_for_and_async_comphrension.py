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


# a very simple async generator
async def doubler(n):
    for i in range(n):
        yield i, i * 2
        await asyncio.sleep(0.1)


async def f(x):
    await asyncio.sleep(0.1)
    return x + 100


async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield f, x


async def async_for_comphrension_demo():
    """
    It’s the async for that makes a comprehension an async comprehension, not the presence of await. All that’s
    needed for await to be legal (inside a comprehension) is for it to be used inside the body of a coroutine
    function—i.e., a function declared with async def. Using await and async for inside the same list comprehension
    is really combining two separate concepts :return:
    """
    result = [x async for x in doubler(3)]
    print(result)

    """First, the factory(3) call returns an async generator, which must be driven by iteration. Because it’s an 
    async generator, you can’t just use for; you must use async for. The values produced by the async generator are a 
    tuple of a coroutine function f and an int. Calling the coroutine function f() produces a coroutine, which must 
    be evaluated with await. Note that inside the comprehension, the use of await has nothing at all to do with the 
    use of async for: they are doing completely different things and acting on different objects entirely. """
    results = [await f(x) async for f, x in factory(3)]
    print('results = ', results)


def demo():
    asyncio.run(demo_async_for())
    asyncio.run(async_for_comphrension_demo())
