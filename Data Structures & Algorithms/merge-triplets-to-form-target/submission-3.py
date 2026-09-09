class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0

        for t in triplets:
            x = x or t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]
            y = y or t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2]
            z = z or t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2]
            if x and y and z:
                return True
        return False