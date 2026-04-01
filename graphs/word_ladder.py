# Problem: Word Ladder
# Pattern: graph traversal (BFS)
# Approach:
# - Build pattern-based adjacency mapping using wildcard '*'
# - Use BFS starting from beginWord
# - Explore all one-letter transformations level by level
# - The first time endWord is reached gives the shortest sequence length
# Time complexity: O(N * M^2), where N is number of words and M is word length
# Space complexity: O(N * M)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[: j] + "*" + word[j+1: ]
                nei[pattern].append(word)
        
        visit = set()
        res = 1
        q = deque([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[: j] + "*" + word[j+1: ]
                    for neighbor in nei[pattern]:
                        if not neighbor in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0
