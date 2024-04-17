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
                    quit()
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
