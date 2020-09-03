"""
It cannot be possible to modify some functions to return coroutines, example functions from external libs.
In such cases, an executor can be used.
"""
import asyncio
import requests


def demo():
    async def main():
        loop = asyncio.get_event_loop()
        # The signature is AbstractEventLoop.run_in_executor(executor, func, *args).
        # If you want to use the default executor (which is a ThreadPoolExecutor), you must pass None as the value for the executor argument.
        future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
        future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
        response1 = await future1
        response2 = await future2
        print(response1.status_code)
        print(response2.status_code)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


demo()
