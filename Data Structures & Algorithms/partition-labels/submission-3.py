class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        length = end = 0
        for i, c in enumerate(s):
            length += 1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(length)
                length = 0
        return res