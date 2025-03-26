from typing import Optional
from Python.ListNode import ListNode

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    my_set = set()
    curr = head
    if curr:
        my_set.add(head.val)

    while curr and curr.next:
        if curr.next.val in my_set:
            curr.next = curr.next.next
        else:
            my_set.add(curr.next.val)
            curr = curr.next
    return head

ListNode.print_linked_list(deleteDuplicates(ListNode.build_linked_list([1, 1, 2])))
ListNode.print_linked_list(deleteDuplicates(ListNode.build_linked_list([1,1,2,3,3])))