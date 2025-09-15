# Import the Node class you created in node.py
from node import Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty.")
            return
        while current:
            print(f"-{current.value}")
            current = current.next #upadte current to next value


def run_help_desk():
    # Create an instance of the Queue class
    helpdesk_queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            if name:
                helpdesk_queue.enqueue(name)
                print(f"{name} was added to the queue.")
            else:
                print("Invalid name. Try again.")
            
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = helpdesk_queue.dequeue()
            if name is None:
                print("No customer in the queue.")
            else:
                print(f"Helped customer {name}")      

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = helpdesk_queue.peek()
            if name is None:
                print("No customers in the queue.")
            else:
                print(f"Next customer is: {name}")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            helpdesk_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
