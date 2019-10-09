import threading
import time
from threading import Thread


def print_func(msg):
    print(msg, '- falling asleep for 3 seconds')
    time.sleep(3)
    print(msg, '- awake!')
    print('Following is the main thread - ', threading.main_thread())       # get reference to main thread from a different thread


class ThreadClass(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print('Running from subclass of thread!')


def demo():
    # 3 different ways of creating a thread
    func_new_thread = Thread(target=print_func, args=('Printing from a different thread',))
    lambda_thread = Thread(target=lambda x, y: print('Result of adding in a new thread = ', x + y), args=(1, 2))
    class_thread = ThreadClass()

    func_new_thread.start()
    lambda_thread.start()
    class_thread.start()

    print('Current thread - ', threading.current_thread())      # MainThread
    print('Enumerate threads - ', threading.enumerate())

    func_new_thread.join()
    lambda_thread.join()
    class_thread.join()
