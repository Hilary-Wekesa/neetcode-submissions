class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_lst=[]
        for s in strs:
            encoded_lst.append(str(len(s)))
            encoded_lst.append("#")
            encoded_lst.append(s)
        return "".join(encoded_lst)
        
    def decode(self, s: str) -> List[str]:
        decoded_lst=[]
        pointer=0
        while pointer<len(s):
            delimiter_index=pointer
            while s[delimiter_index]!="#":
                delimiter_index+=1
            length=int(s[pointer:delimiter_index])
            pointer=delimiter_index+1
            delimiter_index=pointer+length
            decoded_lst.append(s[pointer:delimiter_index])
            pointer=delimiter_index
            
        return decoded_lst