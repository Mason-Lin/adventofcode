from pathlib import Path

moves = Path("data.txt").read_text().splitlines()
print(len(moves))
depth = horizontal = aim = 0

for m in moves:
    move, step = m.split()

    step = int(step)
    if move == "up":
        aim -= step
    elif move == "down":
        aim += step
    elif move == "forward":
        horizontal += step
        depth += step * aim
print(depth, horizontal, aim, horizontal * depth)
