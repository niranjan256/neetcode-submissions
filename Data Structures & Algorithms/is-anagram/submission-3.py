class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,s2 = {},{}
        for char in s:
            s1[char] = s1.get(char,0)+1
        for char in t:
            s2[char] = s2.get(char,0)+1
        return s1==s2
        

