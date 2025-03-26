from Python.ListNode import ListNode
from typing import List, Optional


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = res = ListNode()
    while list1 and list2:               
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2
            
    if list1 or list2:
        cur.next = list1 if list1 else list2
        
    return res.next

ListNode.print_linked_list(mergeTwoLists(ListNode.build_linked_list([1,2,4]), ListNode.build_linked_list([1,3,4])))
ListNode.print_linked_list(mergeTwoLists(ListNode.build_linked_list([]), ListNode.build_linked_list([])))
ListNode.print_linked_list(mergeTwoLists(ListNode.build_linked_list([]), ListNode.build_linked_list([0])))