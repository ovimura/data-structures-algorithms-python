class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, idx):
        return (idx-1) // 2


    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]


    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap)-1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, idx):
        max_index = idx
        while True:
            left_idx = self._left_child(idx)
            right_idx = self._right_child(idx)

            if left_idx < len(self.heap) and self.heap[left_idx] > self.heap[max_index]:
                max_index = left_idx
            if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[max_index]:
                max_index = right_idx
            if max_index != idx:
                self._swap(idx, max_index)
                idx = max_index
            else:
                return


myHeap = MaxHeap()

myHeap.insert(95)
myHeap.insert(75)
myHeap.insert(80)
myHeap.insert(55)
myHeap.insert(60)
myHeap.insert(50)
myHeap.insert(65)
print(myHeap.heap)
myHeap.remove()
print(myHeap.heap)
myHeap.remove()
print(myHeap.heap)
