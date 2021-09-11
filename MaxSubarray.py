class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #set maxsub to start at first value of array
        maxSub = nums[0]
        #set sum to 0
        currSum = 0
        
        #loop through each element in array
        for n in nums:
            #if currSum is negative
            if currSum < 0:
                #reset count to 0
                currSum = 0
            #otherwise add number     
            currSum += n
            #get max between maxsub and currsum
            maxSub = max(maxSub, currSum)
            
        return maxSub
