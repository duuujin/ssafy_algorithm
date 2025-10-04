class MinHeap:
    def __init__(self):
        self.heap = []  

    def heappush(self, item):
        self.heap.append(item)  
        self._siftup(len(self.heap) - 1) 

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("힙이 비었습니다.")  
        if len(self.heap) == 1:
            return self.heap.pop() 
        root = self.heap[0]  
        self.heap[0] = self.heap.pop() 
        self._siftdown(0) 
        return root  

    def heapify(self, array):
        self.heap = array[:]  
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._siftdown(i) 

    def _siftup(self, idx):
        parent = (idx - 1) // 2 
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx] 
            idx = parent  
            parent = (idx - 1) // 2  


    def _siftdown(self, idx):
        n = len(self.heap)
        smallest = idx  
        left = 2 * idx + 1  
        right = 2 * idx + 2  

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left 
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right 
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]  
            self._siftdown(smallest) 

    def __str__(self):
        return str(self.heap)  

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]
