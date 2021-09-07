class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #set lenght to zero 
        lenght = 0 
        
        #if lenght of array is 0, return 0
        if len(nums) == 0:
            return lenght 
        
        #loop through 1 and lenght of array and get each element
        for i in range(1,len(nums)):
            if nums[lenght] < nums[i]:
                
                #add count to lenght for each number in lenght less than element
                lenght += 1
                #otherwise set number to that index
                nums[lenght] = nums[i]
                
        return lenght+1
