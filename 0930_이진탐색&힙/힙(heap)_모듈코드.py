## heap으로 최소 값 구현
import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]


heapq.heapify(numbers)  # 결과: [1, 3, 4, 10, 8, 7, 5]

heapq.heappush(numbers, -1) # 결과: [-1, 1, 4, 3, 8, 7, 5, 10]

smallest = heapq.heappop(numbers)   # 결과: -1, 힙 상태: [1, 3, 4, 10, 8, 7, 5]

print(smallest)

# heqpq로 최대 힙 구현
# heapq 모듈은 회소힙으로 구현되어 있다.
# 최대합을 사용하고 싶으면 어떻게 하느냐 --> 모든 값을 음수로 변환하여 최대 힙처럼 사용

numbers = [10, 1, 5, 3, 8, 7, 4]

max_heap = []
for number in numbers:
    heapq.heappush(max_heap, -number)

print(max_heap) # 최대 힙 출력: [-10, -8, -7, -1, -3, -5, -4]

largest = -heapq.heappop(max_heap)  # 가장 큰 값 반환 : 10

print(largest)
