


def lengthOfLongestSubstring(s):
    # Set to store the characters in the current window
   # 1 initializations set
    char_set = set()

    #2 initialize left window
    left = 0

    #3 initialize right window
    max_length = 0



    #4 loop through the length of the string
    for right in range(len(s)):
        #4.1 If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        #4.2 Add the current character to the set
        char_set.add(s[right])
        
        #4.3 Update the maximum length of the substring found
        max_length = max(max_length, right - left + 1)
    
    # 5 return the max_length
    return max_length

# Example 1
s1 = "abcabcbb"
print(lengthOfLongestSubstring(s1))  # Output: 3

# Example 2
s2 = "bbbbb"
print(lengthOfLongestSubstring(s2))  # Output: 1

# Example 3
s3 = "pwwkew"
print(lengthOfLongestSubstring(s3))  # Output: 3
