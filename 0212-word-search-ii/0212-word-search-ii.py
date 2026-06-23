class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
    
    def addWord(self,word):
        curr=self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        
        row,col=len(board),len(board[0])
        res,visit=set(),set()

        def dfs(node,r,c,word):
            if r<0 or c<0 or r==row or c==col or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.end:
                res.add(word)
            

            dfs(node,r+1,c,word)
            dfs(node,r-1,c,word)
            dfs(node,r,c+1,word)
            dfs(node,r,c-1,word)
            visit.remove((r,c))
        
        for r in range(row):
            for c in range(col):
                dfs(root,r,c,'')
        
        return list(res)



        