from pathlib import Path
from typing import List

filename = "sample.txt"
filename = "data.txt"
data = Path(__file__).parent.joinpath(filename).read_text()

timers = list(map(int, data.split(",")))
total_days = 80
print(f"Initial state: {timers}")


def get_new_timer(timers: List[int]):
    timers = [t - 1 for t in timers]
    new_timers: List[int] = []
    count_new_timers = 0
    for t in timers:
        if t == -1:
            new_timers.append(6)
            count_new_timers += 1
        else:
            new_timers.append(t)
    for _ in range(count_new_timers):
        new_timers.append(8)
    return new_timers


for day in range(total_days):
    timers = get_new_timer(timers)
    # print(f"After  {day+1} day: {timers}")
print(len(timers))
