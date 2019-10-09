"""
Lock can only be acquired once. It cannot be acquired again, until it is released. (After it's been released, it can be re-acaquired by any thread).

An RLock on the other hand, can be acquired multiple times, by the same thread. It needs to be released the same number of times in order to be "unlocked".
In the locked state, some thread owns the lock; in the unlocked state, no thread owns it. To lock the lock, a thread calls its acquire() method; this returns once
the thread owns the lock. To unlock the lock, a thread calls its release() method. acquire()/release() call pairs may be nested; only the final release()
(the release() of the outermost pair) resets the lock to unlocked and allows another thread blocked in acquire() to proceed.

Another difference is that an acquired Lock can be released by any thread, while an acquired RLock can only be released by the thread which acquired it.

-----

* Using locks, conditions, and semaphores in the with statement:

with some_lock:
    # do something...

is equivalent to:

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()

Currently, Lock, RLock, Condition, Semaphore, and BoundedSemaphore objects may be used as with statement context managers.
"""
import threading
import time
from threading import Lock, RLock, Thread


class ThreadLocal:
    """
    Thread-local data is data whose values are thread specific. To manage thread-local data, just create an instance of local (or a subclass) and store attributes on it.
    A threading.local() object only needs to be created once, not once per thread nor once per function call. The global or class level are ideal locations.
    """
    thread_local_data = threading.local()

    def add_and_print_x(self, x):
        if not hasattr(self.thread_local_data, 'x'):
            self.thread_local_data.x = x
        else:
            self.thread_local_data.x += x

        print('X is {} in thread local data for thread {}'.format(self.thread_local_data.x, threading.current_thread().getName()))


def demo():
    lock_demo()

    print('\nR Lock demo begins ... ')
    r_lock_demo()

    print('\nThread local demo begins ... ')
    thread_local_enabled_object = ThreadLocal()
    thread_local_enabled_object.add_and_print_x(1)
    Thread(target=lambda thread_local_enabled_obj, x: thread_local_enabled_obj.add_and_print_x(x), args=(thread_local_enabled_object, 1)).start()


def release_lock(lock, sleep_sec):
    time.sleep(sleep_sec)
    print('Releasing lock {} in thread {} after {} seconds'.format(lock, threading.current_thread(), sleep_sec))
    lock.release()


def lock_demo():
    lock = Lock()
    lock.acquire()

    print('Lock after 1 acquire = {}'.format(lock))

    Thread(target=release_lock, args=(lock, 0)).start()

    lock.acquire()          # this will NOT cause the program to be stuck since the lock has been released in the thread above
    lock.release()
    # lock.release()            # will raise RuntimeError: release unlocked lock


def r_lock_demo():
    r_lock = RLock()          # reentrant lock

    r_lock.acquire()
    r_lock.acquire()          # RLocks can be acquired as many times as desired by the same thread, this will NOT cause the program to get stuck here

    print('RLock after 2 acquires = {}'.format(r_lock))

    # will raise RuntimeError: cannot release un-acquired lock, since the R Lock belongs to a different thread
    # thread = Thread(target=release_lock, args=(r_lock, 0)).start()
    # thread.start()
    # thread.join()

    r_lock.release()
    r_lock.release()
    # r_lock.release()        # will raise RuntimeError: cannot release un-acquired lock
    print('RLock after 2 acquires and 2 releases = {}'.format(r_lock))
