from pathlib import Path
moves = Path("data.txt").read_text().splitlines()
print(len(moves))
depth = horizontal = 0
for m in moves:
    move, step = m.split()
    # print(move, step)
    step = int(step)
    if move == "forward":
        horizontal += step
    elif move == "down":
        depth += step
    elif move == "up":
        depth -= step
print(depth, horizontal, horizontal * depth)

