class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_st=[]
        for s in strs:
            encoded_st.append(str(len(s))+'#'+s)

        
        return ''.join(encoded_st)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1
            word=s[j:length+j]
            res.append(word)
            i=length+j

        return res
            
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))