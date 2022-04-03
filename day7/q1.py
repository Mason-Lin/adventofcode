from pathlib import Path

# filename = "sample.txt"
filename = "data.txt"
data = Path(__file__).parent.joinpath(filename).read_text()

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
best_position = 0
costs = None
positions = sorted(positions)
for try_position in positions:
    sum = 0
    for p in positions:
        sum += abs(p - try_position)

    if costs is None:
        costs = sum
        best_position = try_position

    if sum < costs:
        # update when eq?
        costs = sum
        best_position = try_position

print(f"Best position {best_position}, costs {costs}")
