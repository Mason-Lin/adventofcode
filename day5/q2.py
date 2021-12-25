import math
import re
from collections import Counter
from pathlib import Path

filename = "sample.txt"
# filename = "data.txt"
data = Path(__file__).parent.joinpath(filename).read_text().splitlines()


class Point:
    def __init__(self, x_init, y_init):
        self.x = int(x_init)
        self.y = int(y_init)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self):
        # return "".join(["Point(", str(self.x), ",", str(self.y), ")"])
        return f"{str(self.x)},{str(self.y)}"


class Vent:
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end
        self.path = self.calc_path()

    def calc_path(self):
        if not self.is_considered():
            return []
        if self.is_vertical():
            path = []
            min_x, max_x = sorted([self.begin.x, self.end.x])
            for i in range(int(min_x), int(max_x) + 1):
                p = Point(i, self.begin.y)
                path.append(p)
            return path
        if self.is_horizontal():
            path = []
            min_y, max_y = sorted([self.begin.y, self.end.y])
            for i in range(int(min_y), int(max_y) + 1):
                p = Point(self.begin.x, i)
                path.append(p)
            return path
        if self.is_diagonal():
            path = []
            begin_hypot = math.hypot(self.begin.x, self.begin.y)
            end_hypot = math.hypot(self.end.x, self.end.y)
            if begin_hypot < end_hypot:
                bigger = "end"
            else:
                bigger = "begin"

            if self.begin.x > 0 and self.begin.y > 0:
                quadrant = "1"
            if self.begin.x < 0 and self.begin.y > 0:
                quadrant = "2"
            # quadrant 1
            # quadrant 2
            # quadrant 3
            # quadrant 4
            return []

    def is_considered(self):
        assert not (self.is_vertical() and self.is_horizontal()), "same point??"
        return self.is_vertical() or self.is_horizontal() or self.is_diagonal()

    def is_vertical(self):
        return self.begin.y == self.end.y

    def is_horizontal(self):
        return self.begin.x == self.end.x

    def is_diagonal(self):
        return abs(self.begin.x - self.end.x) == abs(self.begin.y - self.end.y)

    def __repr__(self):
        return f"begin: {self.begin}, end: {self.end}, path: {self.path}"


num_detector = re.compile(r"\d+")
vents = []
for vent_data in data:
    nums = num_detector.findall(vent_data)
    begin = Point(nums[0], nums[1])
    end = Point(nums[2], nums[3])
    vent = Vent(begin, end)
    vents.append(vent)

total_points = []
for v in vents:
    total_points.extend(v.path)
set_points = set(total_points)

records = Counter()
for v in vents:
    for p in v.path:
        records.update([p])


overlap_record = [point for point, count in records.items() if count > 1]
print(len(overlap_record))
