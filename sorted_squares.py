from typing import List

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k= j
        result = [0]* len(nums)
        
        while i <=j:
            left_square = nums[i]*nums[i]
            right_square = nums[j]*nums[j]
            if(left_square > right_square):
                result[k] = left_square
                i+=1
            else:
                result[k] = right_square
                j-=1
            k-=1
        return result
    
solution = Solution1()

# Prepare the test case
test_case = [-4,-1,0,5,10]

# Call the reverseString method


# Print the modified list
print(solution.sortedSquares(test_case))  # Output should be 