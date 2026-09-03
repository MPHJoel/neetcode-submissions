class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key = number, value = index
        seen = dict()
        for i, v in enumerate(nums):
            if (target-v) in seen.keys():
                return [min(i,seen[target - v]),max(i,seen[target - v])]
            seen[v] = i
        print("something went wrong")