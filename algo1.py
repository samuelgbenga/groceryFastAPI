#10 problems
# heap algorithm
# sliding window
# merge sort
# binary search
# greedy

#tomorrow
# linked list
# stack
# set
# graph
# Back Tracking

# the next day
# 10 math algorithm
from heapq import heappop, heappush
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # this is required to compare the ListNode objects in the heap
        return self.val < other.val

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    # 1 initialize empty list
    min_heap = []
    
    # 2 Initialize the heap with the head of each linked list
    for i in range(len(lists)):
        if lists[i]:
            heappush(min_heap, lists[i])
    
    # 3 initialize another linklist loop process: Dummy head for the result list
    head = ListNode(0)
    current = head
    
    # 4 loop through the node without any conversion
    while min_heap:
        # 4.1 Pop the smallest element from the heap
        node = heappop(min_heap)
        
        # 4.2 Add it to the result list
        current.next = node
        current = current.next 
        # Push the next node of the current list (if any) into the heap
        if node.next:
            heappush(min_heap, node.next)
    
    # return the head.next
    return head.next



# Helper function to convert list to ListNode
def to_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert ListNode to list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
lists: List = [
    to_linked_list([1,4,5]),
    to_linked_list([1,3,4]),
    to_linked_list([2,6])
]

merged_list = mergeKLists(lists)
print(to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]


