class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        

        m = len(beginWord)
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromStart, fromEnd = {beginWord : 1}, {endWord : 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromStart, fromEnd = fromEnd, fromStart
            for _ in range(len(qb)):
                word = qb.popleft()
                step = fromStart[word]
                for i in range(m):
                    for c in range(ord("a"), ord("z") + 1):
                        if word[i] == chr(c):
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return step + fromEnd[nei]
                        if nei not in fromStart:
                            fromStart[nei] = step + 1
                            qb.append(nei)
        return 0