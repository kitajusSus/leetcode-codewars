class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        sorted_People = sorted(people, reverse=True, key=lambda x: x[0])
        sorted_names = [name for height, name in sorted_People]
        
        return sorted_names
