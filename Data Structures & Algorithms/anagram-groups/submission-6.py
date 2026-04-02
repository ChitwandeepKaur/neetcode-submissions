class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(0, len(strs)):
            freq_arr = [0] * 26
            for j in range(0, len(strs[i])):
                freq_arr[ord(strs[i][j]) - ord('a')] += 1
            if tuple(freq_arr) in anagrams:
                anagrams[tuple(freq_arr)].append(strs[i])
            else:
                anagrams[tuple(freq_arr)] = [strs[i]]

        return list(anagrams.values())