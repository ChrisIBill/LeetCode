from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print("")
        groups = [[]]
        # while elem = pop strs
        # while j = pop next str
        # isAnagram?
        # push j to groups[index]
        # else push j to groups[index+1]
        for s in strs:
            t = next(s)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        DictS = {}
        for i in range(len(s)):
            DictS[s[i]] = DictS.get(s[i], 0) + 1
            DictS[t[i]] = DictS.get(t[i], 0)-1
        return all(value == 0 for value in DictS.values())
