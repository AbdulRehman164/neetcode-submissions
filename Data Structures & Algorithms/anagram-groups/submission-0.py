from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)  # {sorted_string : [all, the, anagrams], ...}
        for i in range(len(strs)):
            map["".join(sorted(strs[i]))].append(strs[i])
        res = []
        for key in map:
            res.append(map[key])
        return res
