import hashlib
from sortedcontainers import SortedSet
class Solution:
    def create_dict_of_letters(self, st: str) -> dict[str,int]:
        dct = {}
        for char in st:
            if char not in dct.keys():
                dct[char] = 1
            else:
                dct[char] += 1
        return dct

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        ans = []
        count = 0
        for s in strs:
            st = list(s)
            st.sort()
            sts = str(st)
            md5h = hashlib.md5(sts.encode()).hexdigest()
            if md5h not in seen:
                seen[md5h]=count
                ans.append([s])
                count+= 1
            else:
                ans[seen[md5h]].append(s)
        return ans