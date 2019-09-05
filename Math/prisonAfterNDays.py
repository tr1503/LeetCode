# The period is 14 and use this period to get the mod and solve this problem quickly
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        count = 0
        N %= 14
        if N == 0:
            N = 14
        while count < N:
            newCell = [0] * 8
            for i in range(1,7):
                if cells[i - 1] == cells[i + 1]:
                    newCell[i] = 1
                else:
                    newCell[i] = 0
            cells = newCell
            count += 1
        return cells
