"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log.
      i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

import random


class LastOrders:
    def __init__(self, N, *args, **kwargs):
        self.N = N
        self.orders = []

    def record(self, order_id):
        self.orders.append(order_id)
        self.orders = self.orders[-self.N:]

    def get_last(self, i):
        return self.orders[-i:]


if __name__ == '__main__':
    last_orders = LastOrders(N=10)
    order_id = 168
    last_orders.record(order_id)
    for _ in range(20):
        order_id = random.randint(0, 1000)
        last_orders.record(order_id)
        n = 3
        print(order_id)
        print(last_orders.get_last(n))
        print()
