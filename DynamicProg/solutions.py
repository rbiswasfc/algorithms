from typing import List


class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        memory = dict()

        def helper(k, memory):
            if k in memory:
                return memory[k]
            if k == 1:
                return 1
            if k == 2:
                return 2
            ans = helper(k - 2, memory) + helper(k - 1, memory)
            memory[k] = ans
            return ans

        return helper(n, memory)


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # for each house keep track of stash
        dt = [[0, 0] for i in range(N)]
        dt[0][1] = nums[0]

        for i in range(1, N):
            dt[i][0] = max(dt[i - 1][0], dt[i - 1][1])
            dt[i][1] = dt[i - 1][0] + nums[i]

        return max(dt[-1])


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        def helper(stash):
            N = len(stash)
            dt = [[0, False], [stash[0], True]]

            for i in range(1, N - 1):
                new_dt = [[0, True], [0, True]]
                if dt[1][0] > dt[0][0]:
                    new_dt[0][0] = dt[1][0]
                    new_dt[0][1] = dt[1][1]
                else:
                    new_dt[0][0] = dt[0][0]
                    new_dt[0][1] = dt[0][1]

                new_dt[1][0] = dt[0][0] + stash[i]
                new_dt[1][1] = dt[0][1]
                dt = new_dt.copy()
            # post processing
            # print(dt)
            if not dt[0][1]:
                s = dt[0][0] + stash[-1]
            else:
                s = dt[0][0]
            candidate = max(s, dt[1][0])
            return candidate

        candidate_1 = helper(nums)
        candidate_2 = helper(list(reversed(nums)))
        return max(candidate_1, candidate_2)


class MaxSumArray:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        cur_sum = nums[0]

        for num in nums[1:]:
            cur_sum += num
            cur_sum = max(num, cur_sum)
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        prev_min = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            price = prices[i]
            if price >= prev_min:
                this_profit = price - prev_min
                max_profit = max(max_profit, this_profit)
            else:
                prev_min = price
        return max_profit
