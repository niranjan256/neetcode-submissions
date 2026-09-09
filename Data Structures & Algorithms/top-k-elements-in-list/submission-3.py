class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))

        out = []

        for i in list(sorted_dict)[:k]:
            out.append(i)
        print(out)
        return out
