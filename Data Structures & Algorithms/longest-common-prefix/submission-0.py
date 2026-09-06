class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = []
        for s in strs:
            lens.append(len(s))
        for index in range(min(lens)):
            for word in strs:
                if word[index] != strs[0][index]:
                    return strs[0][:index]
        return strs[0][:min(lens)]
