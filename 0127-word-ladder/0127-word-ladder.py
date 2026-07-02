class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if len(beginWord)!=len(endWord):
            return 0
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        q=deque()
        q.append((beginWord,1))

        while q:
            word,level=q.popleft()
            if word==endWord:
                return level
            
            for i in range(len(word)):
                for c in 'abcdefghijklmonpqrstuvwxyz':
                    newWord=word[:i]+c+word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord,level+1))
        
        return 0
        