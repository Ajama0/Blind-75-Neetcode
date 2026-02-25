class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        """

        [3,4,1,2]. target 5

        we need to be able to find a pair of indices that equal to the target
        but instead of the brute force solution wnhere we compare each value with every other value,
        we can iterate over each array and check if we have already counted it (in our hashmap)

        {3:1 4,2}

        as i know the target, is 5 for instance
        at each value i can check if target - nums[i] exists in my map
        so the key is the index and the value is the value at the iterable
        
        """
        
        X = {} #stores the numbers as the key and the index as the value

        for i in range(len(nums)):
            
            if target - nums[i] in X:
                return [X[target-nums[i]], i]
            else:
                X[nums[i]] = i    

                
                    
    



    



