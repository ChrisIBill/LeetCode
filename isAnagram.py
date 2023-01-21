class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        DictS = {}
        for i in range(len(s)):
            DictS[s[i]] = DictS.get(s[i], 0) + 1
            DictS[t[i]] = DictS.get(t[i], 0)-1
        return all(value == 0 for value in DictS.values())
        # Dict = {}
        # for c in s:
        #     Dict[c] = Dict.get(c, 0)+1

        # print(Dict)
    # loop s
        # if s.c exists in data
        # add 1
        # if t.c
