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

    # 1 initialize empty list to hold the Node List
    min_heap = []
    
    # Initialize the heap with the head of each linked list
    # 2 loop through the parent List ( not the internal )
    for i in range(len(lists)):
        # 2.1 if there is something at i push the head at i into the min_heap while mantaining priority queue order where the least value
        # is placed at the root 
        if lists[i]:
            heappush(min_heap, lists[i])
    
    # 3 get a dummy head
    head = ListNode(0)
    # 4 hold that head as current Node
    current = head
    
    # 5 loop through the heap while there is something in min_heap
    while min_heap:
        # 5.1 Pop the smallest element from the heap
        node = heappop(min_heap)
        
        # 5.2 link up with the node from the head 
        current.next = node

        # 5.3 then move to the next
        current = current.next 

        # 5.4 Push the next node of the current list (if any) into the min_heap
        if node.next:
            heappush(min_heap, node.next)
    
    # 6 return the head.next
    return head.next



# Helper function to convert list to ListNode
def to_linked_list(lst):
    # 1 get the head with next equal zero
    head = ListNode(lst[0])
    # 2 hold the head for now
    current = head
    # 3 loop through the rest of the list by point to the next (so on and so forth)
    for value in lst[1:]:
        # 3.1 point to next value (that is not head)
        current.next = ListNode(value)
        # 3.2 move to the next node
        current = current.next
    # 4 return head after creating the link between all the value in the simple list
    return head

# Helper function to convert ListNode to list
def to_list(node):
    # 1 init an empty list
    result = []
    # 2 loop through Node
    while node:
        # 2.1 append the value to the list
        result.append(node.val)
        # 2.2 move to the next node
        node = node.next
    # 3 return Result
    return result



# Example usage:
lists: List = [
    to_linked_list([1,4,5]),
    to_linked_list([1,3,4]),
    to_linked_list([2,6])
]

merged_list = mergeKLists(lists)
print(to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]


