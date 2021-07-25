from typing import List


class WaterContainer:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height)
        max_vol = 0

        left, right = 0, n - 1

        while left + 1 < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > max_vol:
                max_vol = vol
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        # post
        max_vol = max(max_vol, min(height[left], height[right]) * (right - left))
        return max_vol


class RainTrapper:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n <= 1:
            return 0

        def compute(arr):
            stack = []
            cur_max = arr[0]
            trapped = 0

            for i, h_i in enumerate(arr):
                if h_i < cur_max:
                    stack.append([h_i, cur_max])
                else:
                    while stack:
                        e = stack.pop()
                        trapped += e[1] - e[0]
                    cur_max = h_i
            return trapped, cur_max, stack

        trapped, cur_max, stack = compute(height)
        if len(stack) <= 1:
            return trapped
        else:
            # post process the remaining stack
            leftover = []
            for elem in reversed(stack):
                leftover.append(elem[0])
            leftover.append(cur_max)
            rem, _, _ = compute(leftover)
            return trapped + rem


class Anagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        if len(strs) == 1:
            return [[strs[0]]]

        # else use dp to find embeddings
        n = len(strs)
        embeds = [[0] * 26 for _ in range(n)]
        shift = ord("a")
        for i, name in enumerate(strs):
            for j in range(len(name)):
                embeds[i][ord(name[j]) - shift] += 1
        # print(embeds)
        # match embeddings to form groups
        groups = dict()
        for name, embed in zip(strs, embeds):
            key = "_".join([str(e) for e in embed])
            if key in groups:
                groups[key].append(name)
            else:
                groups[key] = [name]

        # post process to get final result
        result = []
        for k, v in groups.items():
            result.append(v)
        return result


class AnagramsAlt:
    def groupAnagrams(self, strs: List[str]):
        d1 = {}
        for i, s in enumerate(strs):
            a = "".join(sorted(s))
            if a in d1:
                d1[a].append(s)
            else:
                d1[a] = [s]
        return d1.values()


class DuplicateZeros:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = []
        n = len(arr)

        for i, elem in enumerate(arr):
            if elem == 0:
                queue.extend([0, 0])
            else:
                queue.append(elem)
            arr[i] = queue.pop(0)


# Overall
weights = np.ones((len(x_train),))

# Subgroup
weights += (train[identity].fillna(0).values >= 0.5).sum(axis=1).astype(int)

# Background Positive, Subgroup Negative
cond_a = train["target"].values >= 0.5
cond_b = (train[identity].fillna(0).values < 0.5).sum(axis=1) == 0
weights += (cond_a & cond_b).astype(int)

# Background Negative, Subgroup Positive
cond_a = train["target"].values < 0.5
cond_b = (train[identity].fillna(0).values < 0.5).sum(axis=1) >= 1
weights += (cond_a & cond_b).astype(int)

loss_weight = 1.0 / weights.mean()
