class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode) :
    # Base case: if the list is empty or has only one node
    if not head or not head.next:
        return head

    # Function to find the middle of the linked list
    def find_middle(head) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Function to merge two sorted linked lists
    def merge(left, right) :
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

    # Find the middle of the list
    mid: ListNode = find_middle(head)
    right_head:  ListNode = mid.next #type:ignore
    mid.next = None

    # Recursively sort the left and right halves
    left_sorted = sortList(head)
    right_sorted = sortList(right_head)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example 1:
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head = sortList(head)
print_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None

# Example 2:
head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
sorted_head = sortList(head)
print_list(sorted_head)  # Output: -1 -> 0 -> 3 -> 4 -> 5 -> None
