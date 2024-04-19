from stack import Stack
from time import perf_counter_ns
from linkedqueue import LinkedQueue
from linkedlist import LinkedList
from maxheap import MaxHeap
from sheetgenerator import Worksheet


def time_function(func, *args):
    """Returns the time taken to call a function"""

    start = perf_counter_ns()
    func(*args)
    end = perf_counter_ns()

    return end-start


class Timer:
    """A class designed to time different data structures"""

    def __init__(self):
        self.stack = Stack()
        self.linkedqueue = LinkedQueue()
        self.linkedlist = LinkedList()
        self.maxheap = MaxHeap()

    def time_stack_pop(self):
        """Prints the amount of time to pop an element from a stack at intervals of 1,000"""

        ws = Worksheet("Time to Pop from Stack")
        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add an element 1000 more times
            for i in range(1000):
                self.stack.push(i)

            # Print the recorded time to pop a single element
            # print(f"Time at {iterations} iterations: {self.time_function(self.stack.pop)} ns")

            # Plot the recorded time to pop a single element in the chart
            ws.plot(iterations, time_function(self.stack.pop))

            # Replace the popped element
            self.stack.push(1000)

        ws.create_graph()

    def time_pop_all(self):
        """Prints the amount of time to pop every element from a stack at intervals of 1,000"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add 1000 more elements each time
            for i in range(iterations):
                self.stack.push(i)

            # Create a function to pass into the time_function method
            def pop_all():
                while not self.stack.is_empty():
                    self.stack.pop()

            # Print the recorded time to pop all elements
            print(f"Time at {iterations} iterations: {self.time_function(pop_all)} ns")

    def time_enqueue(self):
        """Prints the amount of time to enqueue elements at intervals of 1,000"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Create a function to pass into the time_function method
            def enqueue_thousand():
                # Add 1000 elements each time and time it
                for i in range(iterations):
                    self.linkedqueue.enqueue(i)

            # Print the recorded time to enqueue an element
            print(f"Time at {iterations} iterations: {self.time_function(enqueue_thousand)} ns")

            # Remove all elements
            while not self.linkedqueue.is_empty():
                self.linkedqueue.dequeue()

    def time_get_0_entry(self):
        """Prints the amount of time to access the first element from a linked list at intervals of 1,000"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add 1000 more elements
            for i in range(1000):
                self.linkedlist.insert(0, 0)

            # Print the recorded time access the first element, with 0 being the index parameter of get_entry
            elapsed_time = self.time_function(self.linkedlist.get_entry, 0)
            print(f"Time at {iterations} iterations: {elapsed_time} ns")

    def time_get_last_entry(self):
        """Prints the amount of time to access the last element from a linked list at intervals of 1,000"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add 1000 more elements
            for i in range(1000):
                self.linkedlist.insert(0, 0)

            # Print the recorded time to access the last element
            elapsed_time = self.time_function(self.linkedlist.get_entry, self.linkedlist.length()-1)
            print(f"Time at {iterations} iterations: {elapsed_time} ns")

    def time_get_all_entries(self):
        """Prints the amount of time to access the all elements from a linked list at intervals of 1,000"""

        # WARNING: THIS TAKES FOREVER
        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add 1000 more elements
            for _ in range(1000):
                self.linkedlist.insert(0, 0)

            # Create a function to pass into the time_function method
            def access_all():
                for i in range(iterations):
                    self.linkedlist.get_entry(i)

            # Print the recorded time to access the last element
            elapsed_time = self.time_function(access_all)
            print(f"Time at {iterations} iterations: {elapsed_time} ns")

    def time_add_to_maxheap(self):
        """Prints the amount of time to add intervals of 1,000 elements to a maxheap"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Create a function to pass into the time_function method
            def add_iterations():
                # Record the time to add 1000 more elements
                for _ in range(iterations):
                    self.maxheap.add(0)

            # Print the recorded time to access the last element
            elapsed_time = self.time_function(add_iterations)
            print(f"Time at {iterations} iterations: {elapsed_time} ns")

            # Remove all iterations for the next timer
            for _ in range(iterations):
                self.maxheap.remove()

    def run(self):
        """Fill each data structure with an increasing number of elements and record a time for each.
        For each method, start with a data size of 1000 then increase by 1000, recording another time, and repeat until
        100,000 elements are reached."""

        while True:
            print(f"\nOperations\n"
                  f"----------\n"
                  f"1) Popping a single item from a stack\n"
                  f"2) Popping all items from a stack\n"
                  f"3) Queue's enqueue\n"
                  f"4) Linked List get_entry at specifically index 0\n"
                  f"5) Linked List get_entry at specifically the last index\n"
                  f"6) Printing all elements in a LinkedList using get_entry\n"
                  f"7) Adding a value to a Max Heap (our list-based implementation\n"
                  f"8) Quit\n")

            choice = input("Quit to make graphs accessible. Which operation would you like to time?\n")

            match choice:
                case "1":
                    self.time_stack_pop()
                case "2":
                    self.time_pop_all()
                case "3":
                    self.time_enqueue()
                case "4":
                    self.time_get_0_entry()
                case "5":
                    self.time_get_last_entry()
                case "6":
                    self.time_get_all_entries()
                case "7":
                    self.time_add_to_maxheap()
                case "8":
                    quit()
                case _:
                    input("\nThat doesn't seem to be a valid input, try entering a number.\nPress enter to continue.")
