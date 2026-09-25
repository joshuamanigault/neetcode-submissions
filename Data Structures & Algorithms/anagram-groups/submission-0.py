class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in temp:
                temp[key] = [s]
            else:
                temp[key].append(s)

        return [value for value in temp.values()]