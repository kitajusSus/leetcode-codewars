class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #default dictionary to store lists of anagrams
        anagram = defaultdict(list) 

        for s  in strs:
            # Sorting the string and use it as the key
            k = tuple(sorted(s))
            # Append the original string to the corresponding list in the dictionary
            anagram[k].append(s)
        # return all the values from dictionary (lists of lists)
        return list(anagram.values())


## link: https://leetcode.com/submissions/detail/1322791116/
