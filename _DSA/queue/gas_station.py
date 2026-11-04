## -------------------- Gas Station Problem ---------------------
class Queue: # TC:O(n) & SC:O(1)
    def gas_station(self, gas: list[int], cost: list[int]) -> int:
        # total gas < total cost -> -1
        if sum(gas) < sum(cost):
            return -1

        start = 0
        curr_gas = 0

        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                st = i + 1
                curr_gas = 0
        return st


q = Queue()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(q.gas_station(gas, cost))