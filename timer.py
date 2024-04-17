from time import process_time_ns
from stack import Stack
from linkedqueue import LinkedQueue
from linkedlist import LinkedList


class Timer:
    """A class designed to time different data structures"""

    def __init__(self):
        self.stack = Stack()
        self.linkedqueue = LinkedQueue()
        self.linkedlist = LinkedList()

    def time_function(self, func):
        """Returns the time taken to call a function"""

        start = process_time_ns()
        func()
        end = process_time_ns()

        return end-start

    def time_stack_pop(self):
        """Prints the amount of time to pop an element from a stack at intervals of 1,000"""

        iterations = 0

        # Increase the number of iterations by 1000 until it reaches 100,000
        for _ in range(100):
            iterations += 1000

            # Add an element 1000 more times
            for i in range(1000):
                self.stack.push(i)

            # Print the recorded time to pop a single element
            print(f"Time at {iterations} iterations: {self.time_function(self.stack.pop)} ns")

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

            choice = input("Which operation would you like to time?\n")

            match choice:
                case "1":
                    self.time_stack_pop()
                case "2":
                    quit()
                case "3":
                    quit()
                case "4":
                    quit()
                case "5":
                    quit()
                case "6":
                    quit()
                case "7":
                    quit()
                case "8":
                    quit()
                case _:
                    input("\nThat doesn't seem to be a valid input, try entering a number.\nPress enter to continue.")
