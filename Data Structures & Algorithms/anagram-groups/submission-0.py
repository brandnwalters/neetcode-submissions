class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #take strs[str] and check if any of the other str in the list are
        #anagrams. If they are add to a list if not add to seperate
        #list
        stored = defaultdict(list)
        for str in strs:
            sortedstr = ''.join(sorted(str))
            stored[sortedstr].append(str)
        return list(stored.values())
        

        

            
