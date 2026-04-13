class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str=[]
        for st in strs:
            encoded_str.append(str(len(st))+'#'+st)
        
        return ''.join(encoded_str)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            
            n=int(s[i:j])
            j+=1
            decoded_str.append(s[j:j+n])
            i=j+n
        
        return decoded_str
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))