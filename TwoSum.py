class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #create dictionary
        prev_map = {}

        for i,n in enumerate(nums):
            #get difference between target and number
            difference = target-n
            if difference in prev_map:
                #return pair of indexes
                return [prev_map[difference],i]
            #if not found, update hashmap
            prev_map[n] = i
