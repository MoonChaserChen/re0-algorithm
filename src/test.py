class Solution:
    def __init__(self, _arr):
        self.arr = sorted(_arr, reverse=True)

    @staticmethod
    def init_from_console():
        return Solution(list(map(int, input().split(" "))))

    def solve(self):
        le = len(self.arr)
        for i in range(le):
            left, right = i + 1, le - 1
            while left < right:
                if self.arr[i] == self.arr[left] + 2 * self.arr[right]:
                    return [self.arr[i], self.arr[left], self.arr[right]]
                elif self.arr[i] < self.arr[left] + 2 * self.arr[right]:
                    left += 1
                else:
                    right -= 1
        return None


print(Solution.init_from_console().solve())
