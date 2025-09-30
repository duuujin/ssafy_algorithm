# heapq의 우선순위 큐 활용 참고 사이트
# https://docs.python.org/ko/3/library/heapq.html#priority-queue-implementation-notes

import heapq

priority_queue = []

heapq.heappush(priority_queue, (3, "3 priority task")) 
heapq.heappush(priority_queue, (1, "1 priority task")) 
heapq.heappush(priority_queue, (2, "2 priority task"))  

print(priority_queue)  

while priority_queue:
    task = heapq.heappop(priority_queue) 
    print(task) 

"""
(1, '1 priority task')
(2, '2 priority task')
(3, '3 priority task')
"""