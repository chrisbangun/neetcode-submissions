class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            max_len = 0
            while s[i] != '#':
                max_len = max_len * 10 + int(s[i])
                i += 1
            i += 1
            word = s[i: i + max_len]
            decoded.append(word)
            i += max_len
        return decoded
