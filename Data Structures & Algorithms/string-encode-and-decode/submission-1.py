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
        while s:
            delimiter_index=s.find("#")
            charcount_in_next=int(s[:delimiter_index])
            next_word=s[delimiter_index+1:delimiter_index+1+charcount_in_next]
            decoded_lst.append(next_word)
            s=s[delimiter_index+1+charcount_in_next:]
        return decoded_lst

