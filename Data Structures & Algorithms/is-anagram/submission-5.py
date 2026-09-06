class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s1,s2 = {},{}
        for char1,char2 in zip(s,t):
            s1[char1],s2[char2] = s1.get(char1,0)+1, s2.get(char2,0)+1
        return s1==s2
        

