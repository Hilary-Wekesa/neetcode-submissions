class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for s in strs:
            encoded_str+=(f"{len(s)}"+"#"+s)
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        decoded_lst=[]
        while s:
            delimiter_index=s.find("#")
            charcount_in_next=int(s[:delimiter_index])
            next_word=s[delimiter_index+1:delimiter_index+1+charcount_in_next]
            decoded_lst.append(next_word)
            s=s[delimiter_index+1+charcount_in_next:]
        return decoded_lst

        # for word in partial_decoded:
        #     word_so_far=""
        #     count_so_far=0
        #     for c in word:
        #         if count_so_far<=charcount_in_next:
        #             word_so_far+=c
        #             count_so_far+=1
        #         else:
        #             charcount_in_next=int(c)
        #             decoded_lst.append(word_so_far)
        # return decoded_lst

