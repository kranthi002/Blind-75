class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in num_dict:
                return (num_dict[target - x], i)
            num_dict[x] = i
