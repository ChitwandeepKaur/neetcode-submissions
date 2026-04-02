class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for string in strs:
            encoded_str += str(len(string)) + '\:' + string
        return encoded_str 
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            delim = s.find('\:', i)
            length = int(s[i:delim])
            sub_str = s[delim + 2: delim + 2 + length]
            decoded_str.append(sub_str)
            i = delim + 2 + length
        return decoded_str