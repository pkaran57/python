"""
A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several
condition variables must share the same lock. The lock is part of the condition object: you don’t have to track it separately.

Other methods must be called with the associated lock held. The wait() method releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all().
Once awakened, wait() re-acquires the lock and returns. It is also possible to specify a timeout.

The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting.
The notify_all() method wakes up all threads waiting for the condition variable.

Note: the notify() and notify_all() methods don’t release the lock; this means that the thread or threads awakened will not return from their wait() call immediately, but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock.

The typical programming style using condition variables uses the lock to synchronize access to some shared state; threads that are interested in a particular change of
state call wait() repeatedly until they see the desired state, while threads that modify the state call notify() or notify_all() when they change the state in such a way
that it could possibly be a desired state for one of the waiters.
"""

from threading import Condition


def demo():
    cv = Condition()

    num = 0
    nums = []

    while True:

        with cv:
            num += 1
            nums.append(num)
            print('Pushed - ', num)
            # By default, wake up one thread waiting on this condition, if any. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.
            # This method wakes up at most n of the threads waiting for the condition variable; it is a no-op if no threads are waiting.
            # Note: an awakened thread does not actually return from its wait() call until it can reacquire the lock. Since notify() does not release the lock, its caller should.
            cv.notify()

        with cv:
            while not nums:
                # Wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.
                # This method releases the underlying lock, and then blocks until it is awakened by a notify() or notify_all() call for the same condition variable in
                # another thread, or until the optional timeout occurs. Once awakened or timed out, it re-acquires the lock and returns.
                cv.wait()
            print('Popped - ', nums.pop())
