"""
    day 7
"""
import functools
from pathlib import Path

# FILENAME = "sample.txt"
FILENAME = "data.txt"
data = Path(__file__).parent.joinpath(FILENAME).read_text(encoding='utf-8')

positions = list(map(int, data.split(",")))
print(f"Initial state: {positions}")

# 1 brute force
# after think about those cases
# avg is not the best
# hot spot is not the best too
# 1 2 3
# 1 1 100
# 1 1 3 3
# 1 1 2 3 3


@functools.cache
def get_cost_by_distance(distance):
    """
    Lookup cost by distance
        {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55, 11: 66, 12: 78}
    Example
        << 9
        >> 45
    """
    if distance < 2:
        return distance
    return get_cost_by_distance(distance - 1) + distance


def get_cost(point_x, point_y):
    "calc cost of two point"
    distance = abs(point_x - point_y)
    return get_cost_by_distance(distance)


positions = sorted(positions)

# best posttion muse within min ~ max
# assume not empty
search_range = range(positions[0], positions[-1] + 1)

# initial best cost
best_position = 0  # pylint: disable-msg=C0103
best_costs = sum([get_cost(p, positions[0]) for p in positions])

for pos in search_range:
    costs = sum([get_cost(p, pos) for p in positions])
    if costs < best_costs:
        # update when eq? no, only costs matters
        best_costs = costs
        best_position = pos

print(f"Best position {best_position}, costs {best_costs}")
