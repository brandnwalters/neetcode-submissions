class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return true if two strings are anagrams of each other
        # true if a string contains same characters as another string
        # make hash table for each string
        #record frequency of letters
        #compare hash tables
        #return true or false
        s_hash: dict[str, int] = {}
        t_hash: dict[str, int] = {}
        for letter in s: 
            if letter in s_hash:
                s_hash[letter] += 1
            elif letter not in s_hash:
                s_hash[letter] = 1
            
        
        for letter in t: 
            if letter in t_hash:
                t_hash[letter] += 1
            elif letter not in t_hash:
                t_hash[letter] = 1
            
        if s_hash == t_hash:
            return True
        return False

    