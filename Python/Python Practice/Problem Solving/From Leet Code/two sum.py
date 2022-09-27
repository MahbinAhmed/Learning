#Two sum - https://leetcode.com/problems/two-sum/
'''This code needs improvement because it has time related issue. In this problem it is mentioned that the code couldn't be O(n^2)'''
#Inefficient--->>>
class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            if len(result)>=1:
                break
            for j in range(len(nums)):
                if i==j:
                    pass
                elif nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
                else:
                    pass
        return result

a = Solution()
print(a.twoSum(nums=[3,2,4],target=6))

def twoSum(nums,target,idx=0):
    if idx==len(nums):
        return 0
    elif nums[idx]>=target:
        return 0
    else:
        pass