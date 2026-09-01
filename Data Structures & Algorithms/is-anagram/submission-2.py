class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return true if two strings are anagrams of each other
        # true if a string contains same characters as another string
        # make hash table for each string
        #record frequency of letters
        #compare hash tables
        #return true or false
        hashs = {}
        hasht = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in hashs:
                hashs[c] = 1
            else:
                hashs[c] += 1
        for c in t:
            if c not in hasht:
                hasht[c] = 1
            else:
                hasht[c] += 1
        return hashs == hasht
    