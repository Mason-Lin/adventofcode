"""
mappings = [8, 7, 6, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0]
statuses = [0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
statuses = [0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0]
statuses = [1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0]
statuses = [1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0]
statuses = [3, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0]
statuses = [2, 3, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0]
statuses = [2, 2, 3, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0]
statuses = [1, 2, 2, 3, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0]
"""

import timeit
from pathlib import Path
from pprint import pprint

filename = "sample.txt"
filename = "data.txt"
data = Path(__file__).parent.joinpath(filename).read_text()

timers = list(map(int, data.split(",")))
total_days = 256
print(f"Initial state: {timers}")


statuses = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
for timer in timers:
    statuses[timer] += 1
pprint(statuses)

start = timeit.default_timer()
for day in range(total_days):
    # calc from 0 to 8
    count_of_zero = statuses[0]
    for key, count in sorted(statuses.items()):
        if key == 0:
            continue
        statuses[key - 1] = statuses[key]
    statuses[6] += count_of_zero
    statuses[8] = count_of_zero
    # print(f"After  {day+1} day: {statuses}")

total = sum(statuses.values())
print(total)
# assert total == 26984457539
end = timeit.default_timer()
print(end - start)
