from typing import List

"""
Given an integer array nums, 
return true if any value appears more than once in the array, otherwise return false.

Input: nums = [1, 2, 3, 3]

Output: true


"""




class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        len_nums = len(nums)
        set_nums = set(nums)
        len_set = len(set_nums)

        if(len_nums != len_set):
            return True

        return False    

#Time Complexity is O(n)
#Space Complexity is O(n)
        
solution = Solution()

print(solution.hasDuplicate([1,2,3,3]))