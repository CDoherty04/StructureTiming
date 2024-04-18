class MaxHeap:
    def __init__(self):
        self._heap = []

    def get_max(self):
        """Returns the top, or max value of the maxheap"""

        # If the heap is empty raise an Index Error
        if len(self._heap) > 0:
            return self._heap[0]
        else:
            raise IndexError

    def length(self):
        """Gets a count of how many elements are in the heap"""

        return len(self._heap)

    def add(self, entry):
        """Adds an element to the maxheap"""

        self._heap.append(entry)

        # Upheap the new value to the parent element
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        """Recursively moves the element at the given index up"""

        if index == 0:
            return

        else:
            # Parent element index
            parent_i = (index-1)//2

            # If the current element is greater than its parent then switch them
            if self._heap[index] > self._heap[parent_i]:
                temp = self._heap[parent_i]
                self._heap[parent_i] = self._heap[index]
                self._heap[index] = temp
                self._upheap(parent_i)

    def remove(self):
        """Removes the first index, or top/max element"""

        # If the heap is empty, raise an Error
        if self.length() == 0:
            raise RuntimeError

        # If there's only one element in the heap, remove it
        elif self.length() == 1:
            self._heap = []

        # When there's more than one element, replace it with the lowest, right-most element and remove it
        else:
            self._heap[0] = self._heap.pop(-1)

            # Upheap the new value to the parent element
            self._downheap(0)

    def _downheap(self, index):
        """Recursively moves the element at the given index down"""

        l_child_i = 2*index+1
        r_child_i = 2*index+2

        # If there is no left child then do nothing
        if l_child_i >= self.length():
            pass

        # If the left child is bigger than the current element then switch them
        elif self._heap[l_child_i] > self._heap[index]:
            temp = self._heap[l_child_i]
            self._heap[l_child_i] = self._heap[index]
            self._heap[index] = temp
            self._downheap(l_child_i)

        # If there is no right child then do nothing
        if r_child_i >= self.length():
            pass

        # If the left child is bigger than the current element (after checking the right) then switch them
        elif self._heap[r_child_i] > self._heap[index]:
            temp = self._heap[r_child_i]
            self._heap[r_child_i] = self._heap[index]
            self._heap[index] = temp
            self._downheap(r_child_i)
