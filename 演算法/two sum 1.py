class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i

        i = 0
        for i in range(len(nums)):
            left = target-nums[i]
            if left in dict and i != dict[left]:
                return [i, dict[left]]

        return []
