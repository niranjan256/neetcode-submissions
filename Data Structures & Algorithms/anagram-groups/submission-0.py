class Solution:
    def groupAnagrams(self, strs):
        group = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in group:
                group[key] = []
            group[key].append(string)
        return list(group.values()) 
