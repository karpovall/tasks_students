class LifeGame:

    def __init__(self, start_board: list[list[int]]) -> None:
        self.board = start_board
        self.rows = len(start_board)
        self.columns = len(start_board[0])

    def _get_new_square(self, a: int, b: int) -> int:
        c = self.board[a][b]

        if a == 0 and b == 0:
            if c == 1:
                return 1
            if c == 0:
                if self.board[a + 1][b + 1] == 2 and self.board[a][b + 1] == 2 and self.board[a + 1][b] == 2:
                    return 2
                elif self.board[a + 1][b + 1] == 3 and self.board[a][b + 1] == 3 and self.board[a + 1][b] == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (
                        self.board[a + 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (
                        self.board[a + 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif a == 0 and b == self.columns - 1:
            if c == 1:
                return 1
            if c == 0:
                if self.board[a + 1][b - 1] == 2 and self.board[a][b - 1] == 2 and self.board[a + 1][b] == 2:
                    return 2
                elif self.board[a + 1][b - 1] == 3 and self.board[a][b - 1] == 3 and self.board[a + 1][b] == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (
                        self.board[a + 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (
                        self.board[a + 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif a == self.rows - 1 and b == self.columns - 1:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a - 1][b - 1] == 2) and (self.board[a][b - 1] == 2) and (self.board[a - 1][b] == 2):
                    return 2
                elif (self.board[a - 1][b - 1] == 3) and (self.board[a][b - 1] == 3) and (self.board[a - 1][b] == 3):
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a - 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (
                        self.board[a - 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a - 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (
                        self.board[a - 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif a == self.rows - 1 and b == 0:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a - 1][b + 1] == 2) and (self.board[a][b + 1] == 2) and (self.board[a - 1][b] == 2):
                    return 2
                elif (self.board[a - 1][b + 1] == 3) and (self.board[a][b + 1] == 3) and (self.board[a - 1][b] == 3):
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a - 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (
                        self.board[a - 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a - 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (
                        self.board[a - 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif a == 0:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a + 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) == 3:
                    return 2
                elif (self.board[a + 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif b == 0:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a + 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b + 1] == 2) + (self.board[a - 1][b] == 2) == 3:
                    return 2
                elif (self.board[a + 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b + 1] == 3) + (self.board[a - 1][b] == 3) == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b + 1] == 2) + (self.board[a - 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b + 1] == 3) + (self.board[a - 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif a == self.rows - 1:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a - 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a - 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a][b - 1] == 2) == 3:
                    return 2
                elif (self.board[a - 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a - 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a][b - 1] == 3) == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a - 1][b + 1] == 2) + (self.board[a][b + 1] == 2) + (self.board[a - 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a][b - 1] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a - 1][b + 1] == 3) + (self.board[a][b + 1] == 3) + (self.board[a - 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a][b - 1] == 3) >= 2:
                    return 3
                else:
                    return 0
        elif b == self.columns - 1:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a - 1][b] == 2) == 3:
                    return 2
                elif (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a - 1][b] == 3) == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a - 1][b] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a - 1][b] == 3) >= 2:
                    return 3
                else:
                    return 0
        else:
            if c == 1:
                return 1
            if c == 0:
                if (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a - 1][b] == 2) + (
                        self.board[a - 1][b + 1] == 2) + \
                        (self.board[a][b + 1] == 2) + (self.board[a + 1][b + 1] == 2) == 3:
                    return 2
                elif (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a - 1][b] == 3) + (
                        self.board[a - 1][b + 1] == 3) + \
                        (self.board[a][b + 1] == 3) + (self.board[a + 1][b + 1] == 3) == 3:
                    return 3
                else:
                    return 0
            if c == 2:
                if 3 >= (self.board[a + 1][b - 1] == 2) + (self.board[a][b - 1] == 2) + (self.board[a + 1][b] == 2) + \
                        (self.board[a - 1][b - 1] == 2) + (self.board[a - 1][b] == 2) + (
                        self.board[a - 1][b + 1] == 2) + \
                        (self.board[a][b + 1] == 2) + (self.board[a + 1][b + 1] == 2) >= 2:
                    return 2
                else:
                    return 0
            if c == 3:
                if 3 >= (self.board[a + 1][b - 1] == 3) + (self.board[a][b - 1] == 3) + (self.board[a + 1][b] == 3) + \
                        (self.board[a - 1][b - 1] == 3) + (self.board[a - 1][b] == 3) + (
                        self.board[a - 1][b + 1] == 3) + \
                        (self.board[a][b + 1] == 3) + (self.board[a + 1][b + 1] == 3) >= 2:
                    return 3
                else:
                    return 0
        return 0

    def get_next_generation(self) -> list[list[int]]:
        if self.columns == 1 and self.rows == 1:
            if self.board[0][0] == 0 or self.board[0][0] == 2 or self.board[0][0] == 3:
                return [[0]]
            else:
                return [[1]]
        elif self.rows == 1:
            k = [
                [1 if self.board[0][i] == 1 else 0 for i in range(self.columns)]
            ]
            return k
        elif self.columns == 1:
            k = [
                [1 if self.board[i][0] == 1 else 0 ] for i in range(self.rows)
            ]
            return k
        self.board = [
            [self._get_new_square(i, j) for j in range(self.columns)] for i in range(self.rows)
        ]
        return self.board
