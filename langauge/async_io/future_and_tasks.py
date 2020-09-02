"""
A Future represents a future completion state of some activity and is managed by the loop. A Task is exactly the
same, but the specific “activity” is a coroutine— probably one of yours that you created with an async def function
plus create_task()

The Future class is actually a superclass of Task, and it provides all of the functionality for interaction with the
loop.

A Future instance may also do the following:
    *   Have a “result” value set (use .set_result(value) to set it and .result() to obtain it)
    *   Be cancelled with .cancel() (and check for cancellation with .cancelled())
    *   Have additional callback functions added that will be run when the future completes

Difference between concurrent vs asyncio Future:

The concurrent.futures library allows you to set up a thread or process pool for concurrent paths of execution. It is
very similar in design to asyncio in that a function is defined and scheduled to execute. During the scheduling a
Future object is returned (note that concurrent.futures.Future objects are similar to, but not compatible with
asyncio.Future objects). The status and return value of the function can then be accessed using the Future object.
The difference is that concurrent asyncio routines run in a single thread of execution, yielding when waiting for I/O
jobs to process (typically), whereas a concurrent.futures routine runs on a thread or process pool. """
import asyncio
from asyncio import Future


def demo():
    f = Future()
    print(f.done())

    async def main(f: asyncio.Future):
        await asyncio.sleep(1)
        f.set_result('I have finished.')
        return 13

    loop = asyncio.get_event_loop()

    fut = asyncio.Future()
    # Schedule the main() coroutine, passing the future
    task = loop.create_task(main(fut))

    print(fut.done())
    print(task.done())

    # Here we use run_until_complete() on a Future instance, rather than a Task instance
    loop.run_until_complete(fut)

    print(fut.done())
    print(task.done())
    print(fut.result())
    print(task.result())
