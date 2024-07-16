class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Create a count of 26 zeros for each letter in the alphabet
            count = [0] * 26
            # Count the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use the count tuple as the key
            key = tuple(count)
            # Append the original string to the corresponding list in the dictionary
            anagrams[key].append(s)
        
        # Return all the values (lists of anagrams) from the dictionary
        return list(anagrams.values())
