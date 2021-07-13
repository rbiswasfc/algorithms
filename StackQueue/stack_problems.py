from typing import List


class MinStackV1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.data.append(val)
        if not isinstance(self.min_val, int):
            self.min_val = val
        else:
            self.min_val = min(self.min_val, val)
        # print(self)
        # print(self.min_val)

    def pop(self) -> None:
        if len(self.data) == 0:
            return
        val = self.data.pop(-1)

        if val == self.min_val:
            if len(self.data) >= 1:
                self.min_val = min(self.data)
            else:
                self.min_val = None
        # print(self.min_val)
        # print(self)

    def top(self) -> int:
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def getMin(self) -> int:
        if not isinstance(self.min_val, int):
            return
        return self.min_val

    def __str__(self):
        return "{!r}".format(self.data)


class MinStackV2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_val = None

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "Stack: {!r}".format(self.data)

    def push(self, val: int) -> None:
        if not isinstance(self.min_val, int):
            self.min_val = val
            self.data.append((val, None))
        elif val < self.min_val:
            self.data.append((val, self.min_val))
            self.min_val = val
        else:
            self.data.append(val)

    def pop(self) -> None:
        if len(self) == 0:
            return
        val = self.data.pop(-1)

        if isinstance(val, tuple):
            self.min_val = val[1]

        # print(self.min_val)
        # print(self)

    def top(self) -> int:
        if len(self) == 0:
            return None
        val = self.data[-1]
        if isinstance(val, tuple):
            val = val[0]
        return val

    def getMin(self) -> int:
        return self.min_val


class DailyTempsOn2:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cur_i = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                this_temp = temperatures[j]
                if this_temp > cur_i:
                    ans[i] = j - i
                    break
        return ans


class DailyTempsOn1:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < j:
                c = stack.pop()
                res[c] = i - c
            stack.append(i)

        return res


class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        open_pars = set(["(", "{", "["])
        char_mapping = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in open_pars:
                stack.append(char)
            elif stack and char_mapping.get(stack[-1], "") == char:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True


class RPN:
    def eval_rpn(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                # print(stack)
            else:
                x1 = stack.pop(-1)
                x2 = stack.pop(-1)
                if t == "+":
                    val = x1 + x2
                elif t == "-":
                    val = x2 - x1
                elif t == "*":
                    val = x1 * x2
                else:
                    if x1 * x2 >= 0:
                        val = x2 // x1
                    else:
                        val = -(-x2 // x1)
                stack.append(val)
                # print(stack)

        assert len(stack) == 1, "invalid expression"
        return stack[0]


class TargetSumWaysBrute:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        leaf_vals = []
        N = len(nums)

        def explore(depth, s, operator):
            if operator == "+":
                s += nums[depth]
            else:
                s -= nums[depth]

            if depth == N - 1:
                leaf_vals.append(s)
                return

            explore(depth + 1, s, "+")
            explore(depth + 1, s, "-")

        explore(0, 0, "+")
        # print(leaf_vals)
        explore(0, 0, "-")
        # print(leaf_vals)
        ans = sum([val == target for val in leaf_vals])
        return ans


class TargetSumWaysDP:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums = [abs(num) for num in nums]
        shift = sum(nums)
        n, m = len(nums), 2 * shift + 1

        if abs(target) > shift:
            return 0

        lookup = [[0] * m for i in range(n)]
        lookup[0][nums[0] + shift] = 1
        lookup[0][-nums[0] + shift] += 1

        for i in range(1, n):
            for j in range(m):
                if j - nums[i] >= 0:
                    lookup[i][j] += lookup[i - 1][j - nums[i]]
                if j + nums[i] < m:
                    lookup[i][j] += lookup[i - 1][j + nums[i]]

        return lookup[n - 1][target + shift]

