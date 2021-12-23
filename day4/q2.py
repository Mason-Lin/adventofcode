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
        self.bingo = False

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

    def already_bingo(self):
        if self.bingo:
            return True

    def just_bingo(self):
        # horizontal
        for i in range(5):
            if all(self.bingo_board[i]):
                return True
        # vertical
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

    def set_bingo(self, order):
        self.bingo = True
        self.order = order


# load data
boards = defaultdict(Board)
index = 0
for draw in data[1:]:
    if draw == "":
        continue
    complete = boards[index].add_row(draw.split())
    if complete:
        index += 1

# start game
bingo_order = 0
for draw in draws:
    last_draw = int(draw)
    for board in boards.values():
        # add new draw to board
        board.draw(draw)

        # skip bingo one
        if board.already_bingo():
            continue

        # check just bingo
        if board.just_bingo():
            board.set_bingo(bingo_order)
            bingo_order += 1

    # all bingo
    if bingo_order == len(boards):
        break

last_order = max([b.order for b in boards.values()])
for board in boards.values():
    if board.order == last_order:
        sum = board.get_sum()

print(sum * last_draw, sum, last_draw)
assert (12738, 193, 66) == (sum * last_draw, sum, last_draw)
