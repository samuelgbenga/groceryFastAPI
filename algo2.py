# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

def findKthLargest(nums, k):

    #1 Initialize a min-heap
    min_heap = []
    
    #2.0 loop through the array
    for num in nums:
        #2.1 Push the current number into the min-heap using heap (aka priority queue smallest first)
        heapq.heappush(min_heap, num)
        
        #2.2 If the size of the min-heap exceeds k, pop the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    #3.0 The root of the min-heap is the k-th largest element
    return min_heap[0]

# Example 1
nums1 = [3,2,1,5,6,4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5

# Example 2
nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
print(findKthLargest(nums2, k2))  # Output: 4
