from collections import deque

# class Queue:
#     def __init__(self, capacity=10):
#         self.capacity = capacity
#         self.items = [None] * capacity
#         self.front = -1
#         self.rear = -1
#
#     def is_full(self):
#         return self.rear == self.capacity - 1
#
#     def enqueue(self, item):
#         if self.is_full():
#             raise IndexError('Queue is Full')
#         self.rear += 1
#         self.items[self.rear] = item
#
#     def is_empty(self):
#         return self.front == self.rear
#
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError('Queue is Empty')
#         self.front += 1
#         item = self.items[self.front]
#         self.items[self.front] = None
#         return item
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError('Queue is Empty')
#         return self.items[self.front + 1]

# queue = Queue()


# class Queue:
#     def __init__(self, capacity=10):
#         self.capacity = capacity + 1
#         self.items = [None] * self.capacity
#         self.front = 0
#         self.rear = 0
#
#     def is_full(self):
#         return (self.rear + 1) % self.capacity == self.front
#
#     def enqueue(self, item):
#         if self.is_full():
#             raise IndexError('Queue is Full')
#         self.rear = (self.rear + 1) % self.capacity
#         self.items[self.rear] = item
#
#     def is_empty(self):
#         return self.front == self.rear
#
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError('Queue is Empty')
#         self.front = (self.front + 1) % self.capacity
#         item = self.items[self.front]
#         self.items[self.front] = None
#         return item
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError('Queue is Empty')
#         return self.items[(self.front + 1) % self.capacity]
#
#
# queue = Queue(10)
# for i in range(30):
#     queue.enqueue(i)
#     if queue.is_full():
#         print(f"is_Full popleft 한 itmes : {queue.items}")
#         queue.dequeue()
#     print(queue.items)