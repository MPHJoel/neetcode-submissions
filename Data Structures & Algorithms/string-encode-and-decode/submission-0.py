class Solution:

        

    def encode(self, strs: List[str]) -> str:
        tokenstart, tokenend = "<$TART>", "<3NDING>"
        encoded = ""
        for st in strs:
            encoded+=tokenstart
            encoded+=st
            #encoded+=tokenend
        return encoded

    def decode(self, s: str) -> List[str]:
        tokenstart, tokenend = "<$TART>", "<3NDING>"
        decoded = []
        parts = s.split(tokenstart)
        return parts[1:]