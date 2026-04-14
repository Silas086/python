"""
给定一个整数数组nums 和一个整数target,返回两个数字的索引,使得它们之和为target.
您可以假设每个输入都只有一个解，并且不能使用同一个元素两次.
输入： nums = [2,7,11,15], target = 9
输出： [0,1]
解释：因为 nums[0] + nums[1] == 9,所以返回 [0, 1].
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    return [i,j]

s = Solution()
result = s.twoSum([2,7,11,15],9)
print(result)
"""
Better soultion:
def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
"""