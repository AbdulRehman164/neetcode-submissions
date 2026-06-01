from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in range(len(strs)):
            groups["".join(sorted(strs[i]))].append(strs[i])
        return list(groups.values())
