from typing import Optional
from ListNode import ListNode

# https://leetcode.com/problems/linked-list-cycle/
def hasCycle(self, head: Optional[ListNode]) -> bool:
    seen = set()
    temp = head
    while temp:
        if temp in seen:
            return True
        seen.add(temp)
        temp = temp.next
    return False


    