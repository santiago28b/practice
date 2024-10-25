from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while(i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        """
        Do not return anything, modify s in-place instead.
        """
solution = Solution()

# Prepare the test case
test_case = ['h', 'e', 'l', 'l', 'o']

# Call the reverseString method
solution.reverseString(test_case)

# Print the modified list
print(test_case)  # Output should be ['o', 'l', 'l', 'e', 'h']