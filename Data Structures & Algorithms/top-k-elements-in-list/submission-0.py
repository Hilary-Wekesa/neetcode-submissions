class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict=defaultdict(int)
        for n in nums:
            frequency_dict[n]+=1
        frequency_dict=dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))
        return list(frequency_dict.keys())[:k]


        