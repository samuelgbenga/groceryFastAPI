

from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def __lt__(self, other):
        return self.value < other.value






def merge_listNode(lists: List[Optional[ListNode]]):
    
    min_heap = []

    for i in range(len(lists)):
        if lists[i]:
            heappush(min_heap, lists[i])
    
    head = ListNode(0)
    current = head

    while min_heap:
        node = heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heappush(min_heap, node.next)
    
    return head.next





# Helper function conver from list to ListNode
def to_linked_list(list):
    head = ListNode(list[0])
    current = head
    for i in list[1:]:
        current.next = ListNode(i)
        current = current.next
    return head



# Helper function convert from ListNode to list
def to_list(node):
    result = []

    while node.next:
        result.append(node.value)
        node = node.next

    return result


# Example usage:
lists: List = [
    to_linked_list([1,4,5]),
    to_linked_list([1,3,4]),
    to_linked_list([2,6])
]

merged_list = merge_listNode(lists)
print(to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]