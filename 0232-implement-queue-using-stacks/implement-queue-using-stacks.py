class MyQueue:

    def __init__(self):
        self.s = []
        self.ss = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        if not self.ss:
            while self.s:
                self.ss.append(self.s.pop())
        return self.ss.pop()

    def peek(self) -> int:
        if not self.ss:
            while self.s:
                self.ss.append(self.s.pop())
        return self.ss[-1]

    def empty(self) -> bool:
        return max(len(self.s), len(self.ss)) == 0

