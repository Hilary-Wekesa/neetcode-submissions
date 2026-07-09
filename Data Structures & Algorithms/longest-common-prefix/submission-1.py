class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word=strs[0]
        char_so_far=0
        prefixExists=True
        prefix_so_far=""
        while prefixExists and char_so_far < len(first_word):
            if all([char_so_far < len(next_word) and first_word[char_so_far]==next_word[char_so_far] for next_word in strs[1:]]):
                prefix_so_far+=first_word[char_so_far]
                char_so_far+=1
            else:
                prefixExists=False
        return prefix_so_far