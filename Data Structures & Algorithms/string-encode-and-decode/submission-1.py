class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result=result+str(len(i))+"#"+i
        return result
    def decode(self, s: str) -> List[str]:
        n=len(s)
        i=0
        final=[]
        while i<n:
            j=i
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            final.append(word)
            i=j+1+length
        return final

        
            



        
