class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i: int = 0
        seen: dict[int, int] = {}
        result: List[int] = []
        for i, num in enumerate(nums):
            difference: int = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i
            i += 1






           