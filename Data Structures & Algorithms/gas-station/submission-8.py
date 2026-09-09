class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        res = 0
        totalCost = 0
        for i in range(len(gas)):
            totalCost += gas[i] - cost[i]
            if totalCost < 0:
                totalCost = 0
                res = i + 1
        return res