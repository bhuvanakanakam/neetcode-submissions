class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we need to map annagrams to the count of the strings
        # first find the annagrams, make a count of the letters
        # there are 26 ones, so have ascii here

        result = defaultdict(list)
        for string in strs:
            count = [0]*26
            for character in string:
                count[ord(character)-ord("a")] += 1
            result[tuple(count)].append(string)
        return list(result.values())