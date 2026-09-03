from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t1 = Counter(t)

        if len(s1-t1) > 0 or len(t1-s1) >0:
            return False
        return True