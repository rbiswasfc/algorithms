from typing import List


class IslandExplorer:
    def count_islands(self, grid: List[List[str]]) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        # print(m)
        # print(n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue.append([i, j])

        def explore(x, y):
            if (x < 0) or (x >= m):
                return
            if (y < 0) or (y >= n):
                return
            if grid[x][y] == "0":
                return

            grid[x][y] = "0"  # set zero to visited node

            explore(x + 1, y)  # go right
            explore(x, y + 1)  # go bottom
            explore(x - 1, y)  # go left
            explore(x, y - 1)  # go top

        num_islands = 0
        # print(len(queue))
        while queue:
            pos = queue.pop(0)
            # print(pos)
            if grid[pos[0]][pos[1]] == "0":
                continue
            num_islands += 1
            explore(pos[0], pos[1])
            # print(grid)

        return num_islands


class OpenTheLock:
    def open_lock(self, deadends: List[str], target: str) -> int:
        # def dist(str1, str2):
        #     n = len(str1)
        #     dist = 0
        #     for i in range(n):
        #         x, y = int(str1[i]), int(str2[i])
        #         this_dist = min(abs(x-y), ((10-max(x,y)) + min(x,y)))
        #         dist += this_dist
        #     return dist

        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        states = [[target]]
        num_hops = 0

        while states:
            nodes = states.pop(0)
            # print(len(nodes))
            num_hops += 1
            next_states = []

            for node in nodes:
                # print(node)
                deadends.add(node)
                candidate = [node[0], node[1], node[2], node[3]]
                for i in range(len(node)):
                    temp = candidate.copy()
                    temp[i] = str((int(temp[i]) + 1) % 10)
                    temp = "".join(temp)
                    if temp not in deadends:
                        next_states.append(temp)

                    temp = candidate.copy()
                    temp[i] = str((int(temp[i]) - 1) % 10)
                    temp = "".join(temp)
                    if temp not in deadends:
                        next_states.append(temp)
            if len(next_states) == 0:
                return -1
            if "0000" in next_states:
                return num_hops
            states.append(list(set(next_states)))


class SumSquares:
    def find_num_squares(self, n):

        # list of square numbers that are less than `n`

        square_nums = [(i * i) for i in range(1, int(n ** 0.5) + 1)]
        queue = {n}
        level = 0

        while queue:
            level += 1
            new_queue = set()

            for remainder in queue:
                for square in square_nums:
                    if remainder == square:
                        return level
                    new_remainder = remainder - square
                    if new_remainder > 0:
                        new_queue.add(new_remainder)

            queue = new_queue

        return level


#### Q using two stacks
class MyStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def empty(self):
        return len(self) == 0

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return
        return self.data.pop()

    def peak(self):
        if self.empty():
            return
        return self.data[-1]


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = MyStack()
        self.s2 = MyStack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2.empty():
            if self.s1.empty():
                return
            else:
                # data transfer
                while not self.s1.empty():
                    e = self.s1.pop()
                    self.s2.push(e)
                return self.s2.pop()
        else:
            return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2.empty():
            if self.s1.empty():
                return
            else:
                while not self.s1.empty():
                    e = self.s1.pop()
                    self.s2.push(e)
                return self.s2.peak()
        else:
            return self.s2.peak()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() & self.s2.empty()

    def __str__(self):
        rep = "s1: {!r}\ns2:{!r}".format(self.s1.data, self.s2.data)
        return rep
