import pprint
from collections import defaultdict
from pathlib import Path

data = Path(__file__).parent.joinpath("data.txt").read_text().splitlines()

draws = data[0].split(",")


class Board:
    def __init__(self):
        self.board = [[], [], [], [], []]
        self.bingo_board = [[False] * 5, [False] * 5, [False] * 5, [False] * 5, [False] * 5]  # 5*5 False
        self.index = 0

    def add_row(self, row):
        self.board[self.index].extend(row)
        self.index += 1
        return True if self.index == 5 else False

    def __repr__(self):
        return "\n" + pprint.pformat(self.board) + "\n" + pprint.pformat(self.bingo_board) + "\n"

    def draw(self, num):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == num:
                    self.bingo_board[i][j] = True

    def just_bingo(self):
        for i in range(5):
            if all(self.bingo_board[i]):
                return True
        for j in range(5):
            count = 0
            for i in range(5):
                if self.bingo_board[i][j]:
                    count += 1
                if count == 5:
                    return True
        return False

    def get_sum(self):
        sum = 0
        for j in range(5):
            for i in range(5):
                if not self.bingo_board[i][j]:
                    sum += int(self.board[i][j])
        return sum


boards = defaultdict(Board)
index = 0
for draw in data[1:]:
    if draw == "":
        continue
    complete = boards[index].add_row(draw.split())
    if complete:
        index += 1

bingo = False
for draw in draws:
    if bingo:
        break
    last_draw = int(draw)
    for board in boards.values():
        board.draw(draw)
        if board.just_bingo():
            print(f"bingo at {draw} and board is {board}")
            sum = board.get_sum()
            bingo = True
            break
# print(boards)
print(sum * last_draw, sum, last_draw)
assert (8136, 678, 12) == (sum * last_draw, sum, last_draw)
