"""
Problem: Insert at Head of Linked List
Description: Implement a function to insert a new node at the beginning of a singly linked 
list. The function should take a value and insert it at the head of the list, updating the 
head of the list.
Example: After inserting 3 into an empty list, the list should contain 3.
"""
from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data: Any) -> None:
        new_node = None(data)
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(5)
    ll.insert_at_head(10)
    current = ll.head
    while current:
        print(current.data)
        current = current.next
