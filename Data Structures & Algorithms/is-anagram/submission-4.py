class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # approach 1 - 2 dicts, O(n) but space is going to be more
        # count_s = {}
        # count_t = {}
        # for character in s:
        #     count_s[character] = count_s.get(character,0) + 1
        # for character in t:
        #     count_t[character] = count_t.get(character, 0) + 1
        # return count_s == count_t

        # approach 2 - have 1 dict, do the count for one loop, and
        # decrease for the other string, if suppose a character has 0
        # value in the count in string 2, return false
        # count = {}
        # for character in s:
        #     count[character] = count.get(character,0) + 1
        # for character in t:
        #     if count.get(character,0) == 0:
        #         return False
        #     count[character] -= 1
        # return True

        # approach 3 - lower case, use ord.
        count = [0] * 26 # populate an array of 0 with 26 elements
        for character1, character2 in zip(s,t):
            count[ord(character1) - ord('a')] += 1
            count[ord(character2) - ord('a')] -= 1
        return all(countvar == 0 for countvar in count)

        # approach 4, inbuilt counter
        # from collections import Counter
        # return counter(s) == counter(t)
