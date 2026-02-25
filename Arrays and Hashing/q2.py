
"""
q2
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

"""


class Solution:
    
    
    def isAnagram(self, s: str, t: str) -> bool:

        #lets first ensure the strings are of the same length

        if(len(s)!=len(t)):
            return False

        #if they are of the same length then we can use a counter dict, to see occurances of elements

        count_s={}

        #now we can loop through each element in S and increment their counter
        #use a count.get() as we check if a key exists and if we does we retrieve that key and add 1 to it, otherwise 0

        for char in range(len(s)):
            count_s[s[char]] = 1 + count_s.get(s[char], 0)
            #now all values in the string are incremented with respect to occurances

        #loop through t string 
        #check if any value of t exists in s, if so decrement it
        for i in t:
            if(i in count_s):
                count_s[i] -=1

            #if any value of count_s[] is a negative then a character occured more in one string compared to the other
                if(count_s[i] < 0):
                    return False


            #if the value of t is in not in s 
            else:
                return False


        return True            

                
#Time complexity O(n)
#Space complexity O(n)


class SecondSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        first you have to check if they are equal in length otherwise return false
        s = racecarr
        t = carrace
        would return false
        
        we can create two dictionaries and append each character with its count
        iterating over both strings gives time complexity o(n+m), therefore you can 
        later compare both dicts to see if they have the same key value pairs

        """

        if(len(s) != len(t)):
            return False
        
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                 s_count[s[i]] +=1
                    

        for j in range(len(t)):
            if t[j] not in t_count:
                t_count[t[j]] = 1

            else:
                t_count[t[j]] += 1


        #we compare the key value pair counts
        print(s_count)
        print(t_count)
        return s_count == t_count

                   
