# Hello -> char_len_
# hello world abcd
# 5##hello123##
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            word_len = len(word)
            encoded.append(f"{word_len}#{word}")
        print(encoded)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            word_len = 0
            while s[i] != '#':
                word_len = word_len * 10 + int(s[i])
                i += 1
            i += 1
            decoded.append(s[i: i + word_len])
            i += word_len
        return decoded
