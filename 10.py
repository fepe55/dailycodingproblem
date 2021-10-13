"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
"""

import time
import threading
from datetime import datetime

START_TIME = datetime.now()


class Scheduler:
    def delay(self, f, args, n):
        milliseconds = n/1000
        time.sleep(milliseconds)
        f(*args)

    def queue(self, f, args, n):
        t = threading.Thread(target=self.delay, args=(f, args, n))
        t.start()


if __name__ == '__main__':
    def some_function(name=None):
        if not name:
            name = 'NONAME'
        print(f'hello {name}')
        time_diff = datetime.now() - START_TIME
        miliseconds = time_diff.total_seconds() * 1000
        print(f'Function executed in {miliseconds} miliseconds since the '
              'start of the execution of this script')

    s = Scheduler()

    f = some_function
    n = 5000
    s.queue(f, ['john'], n)

    print('execution uninterrupted')

    n = 4000
    s.queue(f, ['paul'], n)
