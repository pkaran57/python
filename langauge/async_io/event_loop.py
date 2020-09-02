"""The event loop in asyncio handles all of the switching between coroutines, as well as catching those StopIteration
exceptions—and much more, such as listening to sockets and file descriptors for events.

You can get by without ever needing to work with the event loop directly: your asyncio code can be written entirely
using await calls, initiated by an asyncio.run(coro) call. However, at times some degree of interaction with the
event loop itself might be necessary, and here we’ll discuss how to obtain it. There are two ways:

Recommended
asyncio.get_running_loop(), callable from inside the context of a coroutine

Discouraged
asyncio.get_event_loop(), callable from anywhere

The get_event_loop() method works only within the same thread. In fact, get_event_loop() will fail if called inside a
new thread unless you specifically create a new loop with new_event_loop(), and set that new instance to be the loop
for that thread by calling set_event_loop(). Most of us will only ever need (and want!) a single loop instance
running in a single thread. This is nearly the entire point of async programming in the first place.

In contrast, get_running_loop() (the recommended method) will always do what you expect: because it can be called
only within the context of a coroutine, a task, or a function called from one of those, it always provides the
current running event loop, which is almost always what you want. """
import asyncio


def demo():
    loop = asyncio.get_event_loop()
    loop2 = asyncio.get_event_loop()

    # If you’re inside a coroutine function and you need access to the loop instance, it’s fine to call
    # get_event_loop() or get_running_loop() to obtain it. You do not need to pass an explicit loop parameter through
    # all your functions.
    print(loop is loop2)

    async def sub_co_routine():
        print("From sub_co_routine")

    async def co_routine():
        for i in range(3):
            asyncio.create_task(sub_co_routine())
        print('exit from co_routine')       # this co-routine will be exited before the tasks in line above are run

    asyncio.run(co_routine())
