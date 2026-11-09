class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            index1: int = i + 1
            index2: int = len(nums) - 1
            while index1 < index2:
                if nums[index1] + nums[index2] == -nums[i]:
                    if [nums[i], nums[index1], nums[index2]] not in res:
                        res.append([nums[i], nums[index1], nums[index2]])
                    index1 += 1
                    index2 -= 1
                elif nums[index1] + nums[index2] > -nums[i]:
                    index2 -= 1
                elif nums[index1] + nums[index2] < -nums[i]:
                    index1 += 1
        return res
                

                

            

