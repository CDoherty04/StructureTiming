from node import Node


class LinkedList:

    def __init__(self):
        self._front = None
        self._length = 0

    def length(self):
        return self._length

    def insert(self, index, entry):

        # Check range
        if 0 <= index <= self._length:

            # Create node to be inserted
            new_node = Node(entry)

            # Add to front
            if index == 0:
                new_node.next = self._front
                self._front = new_node
                self._length += 1

            # Add to end
            elif index == self._length:
                jumper = self._front
                for i in range(index-1):
                    jumper = jumper.next
                jumper.next = new_node
                self._length += 1

            # Insert within
            else:
                before_jumper = self._front
                after_jumper = self._front
                for i in range(index-1):
                    before_jumper = before_jumper.next
                for i in range(index):
                    after_jumper = after_jumper.next
                before_jumper.next = new_node
                new_node.next = after_jumper
                self._length += 1

        # Allows appending
        else:
            raise IndexError()

    def get_entry(self, index):
        if 0 <= index < self._length:
            jumper = self._front
            for i in range(index):
                jumper = jumper.next
            return jumper.value
        else:
            raise IndexError()
