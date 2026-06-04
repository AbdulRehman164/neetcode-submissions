class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0

        while pointer < len(s) - 1:
            num = ""
            while s[pointer].isdigit():
                num += s[pointer]
                pointer += 1
            num = int(num)

            if s[pointer] == "#":
                pointer += 1
                word = s[pointer : pointer + num]
                pointer += num
                res.append(word)
        return res
