"""
What is a coroutine?

A coroutine is an object that encapsulates the ability to resume an underlying function that has been suspended
before completion. If that sounds familiar, it’s because coroutines are very similar to generators.
"""
import asyncio
import inspect


def demo():
    async def co_routine_func():
        return 32

    print(type(co_routine_func))
    print('iscoroutinefunction = {}'.format(inspect.iscoroutinefunction(co_routine_func)))

    co_routine = co_routine_func()
    print(type(co_routine))

    """
    When a coroutine returns, what really happens is that a StopIteration exception is raised. A coroutine is initiated
    by “sending” it a None. Internally, this is what the event loop is going to be doing to your precious coroutines;
    you will never have to do this manually. When the coroutine returns, a special kind of exception is raised,
    called StopIteration. Note that we can access the return value of the coroutine via the value attribute of the
    exception itself.
    """
    try:
        co_routine.send(None)
    except StopIteration as e:
        print('The answer was:', e.value)

    # --------------

    """
    keyword await always takes a parameter and will accept only a thing called an awaitable, which is defined as one of
    these (exclusively!):
    1. Any object implementing the __await__() special method. That special method must return an iterator
    2. A coroutine (i.e., the result of a called async def function)
    """

    async def f():
        await asyncio.sleep(1.0)
        return 123

    # Calling f() produces a coroutine; this means we are allowed to await it. The value of the result variable will be
    # 123 when f() completes.
    async def main():
        result = await f()
        return result

    # ----- Using coroutine.throw() to inject exceptions into a coroutine

    """
    when you call task.cancel(), the event loop will internally use coroutine.throw() to raise asyncio.CancelledError 
    inside your coroutine 
    """

    """    
    coroutine = f()
    coroutine.send(None)
    coroutine.throw(Exception, 'blah')
    """

    # ----- Coroutine cancellation with CancelledError

    """Note that the exception is being injected into the coroutine from outside; i.e., by the event loop, which we’re 
    still simulating with manual send() and throw() commands.
     
    Of course, it should go without saying that you should never actually do this! If your coroutine receives a 
    cancellation signal, that is a clear directive to do only whatever cleanup is necessary and exit. Don’t just ignore 
    it. 
    """

    """
    async def f():
        try:
            while True: await asyncio.sleep(0)
        except asyncio.CancelledError:
            print('Nope!')
            while True: await asyncio.sleep(0)
        else:
            return 111

    coroutine = f()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    """
