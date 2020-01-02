'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
'''

'''
It calculates the left multiplication and right multiplication of elements using 2 extra arrays and multiplies it to find the total.

Time Complexity - O(n)
Space Complexity - O(n)
'''
def productExceptSelf(self, nums: List[int]) -> List[int]:
        noNum = len(nums)
        left = [0]*noNum
        right = [0]*noNum
        left[0] = 1
        right[noNum-1] = 1
        for index in range(1, noNum):   
            left[index] = left[index-1] * nums[index - 1]
            right[noNum - (index+1)] = right[noNum - index] * nums[noNum - index]
        
        prod = [0]*noNum
        
        for i in range(noNum):
            prod[i] = left[i] * right[i]
        
        return prod

'''
Using Log addition and subtraction.

this will not work when the value is having 0.
'''
def productExceptSelf(self, nums: List[int]) -> List[int]:
        logVals = 0
        # epsilon value to maintain precision 
        EPS = 1e-9
        for each in nums:
            #print(math.log10(each))
            logVals += math.log10(each)
        
        prod = [0]*len(nums)
        for i in range(len(nums)):
            prod[i] = int((EPS + pow(10.00, logVals - math.log10(nums[i]))))
        
        return prod
