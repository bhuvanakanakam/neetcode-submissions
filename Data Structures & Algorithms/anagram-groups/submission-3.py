from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # letter order doesnt matter, but the charac count matters

      # approach 1 :
      # take a word, make a group, check the next word with the prev    
      # groups, if not make a new group

      # approach 2 : ( time limit exceeded ) - helper function of checking
      # if an annagram exists between two strings.
      # then, have empty list of groups for output, and a flag set to 
      # false. then within each group, check anagram for first element 
      # current string, if it is an annagram - then set flag to true
      # and append to the group, and break the code once loop is over
      # otherwise, append to the groups list as a subgroup

      # time complexity : O(n^2 x k)
      # so try to reduce this to single for loop.

        # def checkAnagram(s1, s2): # O(k)
        #     if len(s1) != len(s2):
        #         return False
        #     count = {}
        #     for character in s1:
        #         count[character] = count.get(character, 0) + 1
        #         # O(k) k is the string length
        #     for character in s2:
        #         if count.get(character,0) == 0:
        #             return False
        #         count[character] -= 1
        #         # O(k)
        #     return True
        # groups = []

        # for string in strs: #O(n^2) x O(k)
        #     found_group = False
        #     # print("string", string)
        #     for group in groups : 
        #         # print("group", group)
        #         if checkAnagram(string, group[0]): 
        #             found_group = True
        #             group.append(string) 
        #             # print ("after anagram check group", group)
        #             # print ("current groups", groups)
        #             break
        #     # after exiting the for loop, checking all groups
        #     if not found_group:
        #         groups.append([string])
        #         # print("appended group", groups)
        # return groups

    # approach 3 : 
    # give each indiviual group, a key. a cannonical / signature key
        groups = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for character in string:
                count[ord(character) - ord("a")] += 1
            groups[tuple(count)].append(string)
        return list(groups.values())















