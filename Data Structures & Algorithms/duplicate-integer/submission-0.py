class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        duplicates = set()
        for num in nums:
            if num not in duplicates:
                duplicates.add(num)
            elif num in duplicates:
                result = True
                return result
        return result
