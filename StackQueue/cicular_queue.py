class MyCircularQueue:
    def __init__(self, k: int):
        assert (k <= 1000) and (k >= 1), "wrong input size"
        self.max_size = k
        self.cur_size = 0
        self.data = [None] * k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if isinstance(self.tail, int):
            en_idx = (self.tail + 1) % self.max_size
            if (en_idx != self.head) or (self.cur_size == 0):
                self.cur_size += 1
                self.data[en_idx] = value
                self.tail = en_idx
                return True
            else:
                return False
        else:
            self.head = 0
            self.tail = 0
            self.data[0] = value
            self.cur_size += 1
            return True

    def deQueue(self) -> bool:
        if self.cur_size > 0:
            self.data[self.head] = None
            self.cur_size -= 1
            # if self.cur_size != 0:
            self.head = (self.head + 1) % self.max_size
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty:
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty:
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.cur_size == 0

    def isFull(self) -> bool:
        return self.cur_size == self.max_size

    def __str__(self):
        cur_data = list(filter(None, self.data))
        s = "Queue with data {} with head and tail at {}, {}".format(
            cur_data, self.head, self.tail
        )
        return s


if __name__ == "__main__":
    k = 5
    obj = MyCircularQueue(k)
    param_1 = obj.enQueue(20)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()
