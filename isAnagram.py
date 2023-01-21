class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        DictS, DictT = {}, {}
        for i in range(len(s)):
            DictS[s[i]] = DictS.get(s[i], 0) + 1
            DictT[t[i]] = DictT.get(t[i], 0)-1
        return DictS == DictT
        # Dict = {}
        # for c in s:
        #     Dict[c] = Dict.get(c, 0)+1

        # print(Dict)
    # loop s
        # if s.c exists in data
        # add 1
        # if t.c
