"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        """
        we create a hashamap that contains the sorted string as the key
        the value is the original word in a list.

        when the next string that contains the same letters comes and we sort it
        we already have the key stored, therefore we append it to that list.

        example

        [cat, act, god, dog]

        sort cat -> act 
        sort act -> act
        sort dog -> dgo
        sort god -> dgo

        {act : [cat, act], dgo :[dog, god] }

        """

        anagrams_dict = {}
        for i in strs:
            i_sorted = "".join(sorted(i))
            if i_sorted in anagrams_dict:
                anagrams_dict[i_sorted].append(i)

            else:
                anagrams_dict[i_sorted] = [i]


        return list(anagrams_dict.values())

                




        