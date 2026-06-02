class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0
        alpmap = {}
        alp2map = {}
        while i < len(s):
            if s[i] not in alpmap and t[i] not in alp2map:
                alpmap[s[i]] = t[i]
                alp2map[t[i]] = 0
            else:
                if alpmap.get(s[i]) == t[i]:
                    print(i, s[i], alpmap.get(s[i]), t[i])
                else:
                    return False
            i = i + 1
        return True