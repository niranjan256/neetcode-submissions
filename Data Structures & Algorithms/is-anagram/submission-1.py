class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        for i,char in enumerate(s):
            s1[char] = s1.get(char,0)+1
        s2={}
        for i,char in enumerate(t):
            s2[char] = s2.get(char,0)+1

        return True if s1==s2 else False
