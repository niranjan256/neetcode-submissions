class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in d:
                d[key] = []
            d[key].append(string)
        return list(d.values())

        