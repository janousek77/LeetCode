from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build_linked_list(values: List) -> Optional['ListNode']:
        """
        Converts a Python list into a linked list.
        
        Args:
            values: List of values to convert into a linked list
            
        Returns:
            The head of the linked list, or None if the input list is empty
        """
        if not values:
            return None
            
        # Create the head node
        head = ListNode(values[0])
        current = head
        
        # Build the rest of the list
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
            
        return head

    def print_linked_list(head: Optional['ListNode']) -> None:
        """
        Prints the linked list values in order.
        
        Args:
            head: The head of the linked list
        """
        values = []
        current = head
        
        while current:
            values.append(str(current.val))
            current = current.next
            
        print(" -> ".join(values))