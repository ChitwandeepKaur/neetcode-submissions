class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charhash = {}
        for word in strs:
            chararr = [0]*26
            for char in word:
                chararr[ord(char) - ord('a')] += 1
            if tuple(chararr) not in charhash:
                charhash[tuple(chararr)] = [word]
            else:
                charhash[tuple(chararr)].append(word)
        ans = []
        for val in charhash.values():
            ans.append(val)

        return ans