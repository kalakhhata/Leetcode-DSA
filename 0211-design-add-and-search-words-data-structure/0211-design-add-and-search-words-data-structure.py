class TrieNode():
    def __init__(self):
        self.children={}
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.end=True
        

    def search(self, word: str) -> bool:
        curr=self.root
        def dfs(j,node):
            
            for i in range(j,len(word)):
                ch=word[i]
                if ch=='.':
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
            
                else:
                    if ch not in node.children:
                        return False
                    node=node.children[ch]
            return node.end

        return dfs(0,curr)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)