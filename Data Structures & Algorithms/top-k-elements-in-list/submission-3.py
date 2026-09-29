from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)

        for num in nums:
            dct[num] += 1
        hp = []
        for item in dct.items():
            hp.append((item[1],item[0]))
        heapq.heapify_max(hp)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop_max(hp)[1])
        return ans
