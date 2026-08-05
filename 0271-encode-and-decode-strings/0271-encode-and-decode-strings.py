class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_l=[]
        for st in strs:
            encode_l.append(str(len(st))+'#'+st)
        
        return ''.join(encode_l)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        st=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1
            word=s[j:length+j]
            st.append(word)
            i=(length+j)
        return st





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))