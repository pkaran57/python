import time
import asyncio

"""Problem: This section examines what happens during shutdown when executor jobs take longer to finish than all the 
pending Task instances. The short answer is: without intervention, you’re going to get errors. What’s happening here 
is that behind the scenes, run_in_executor() does not create a Task instance: it returns a Future. That means it 
isn’t included in the set of “active tasks” that get cancelled inside asyncio.run(), and therefore 
run_until_complete() (called inside asyncio.run()) does not wait for the executor task to finish. The RuntimeError is 
being raised from the internal loop.close() call made inside asyncio.run(). 

At the time of writing, loop.close() in Python 3.8 does not wait for all executor jobs to finish, and this is why the 
Future returned from run_in_executor() complains: by the time it resolves, the loop has already been closed. 

In Python 3.9, the asyncio.run() function has been improved to correctly wait for executor shutdown, but at the time 
of writing, this has not yet been backported to Python 3.8. """


async def error_main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(2)
    print(f"{time.ctime()} Hello from a thread!")


# fix #1:  wrap the executor call inside a coroutine
async def fix_1_main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    try:
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')
    finally:
        await future


# fix #2: add the executor future to the gathered tasks
async def make_coro(future):
    try:
        return await future
    except asyncio.CancelledError:
        return await future


async def fix_2_main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    asyncio.create_task(make_coro(future))
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def demo():
    # asyncio.run(error_main())
    asyncio.run(fix_1_main())
    asyncio.run(fix_2_main())
