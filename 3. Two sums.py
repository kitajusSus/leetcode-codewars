class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers we have seen and their indices
        num_to_index = {}
        
        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_to_index:
                # If found, return the indices
                return [num_to_index[complement], index]
            
            # If not found, add the number and its index to the dictionary
            num_to_index[num] = index
        
        # If no solution is found, return an empty list (shouldn't happen)
        return []
