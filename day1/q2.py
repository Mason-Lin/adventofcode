from pathlib import Path

measurements = Path("data").read_text().splitlines()

print(len(measurements))

sliding = []
# measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
for a, b, c in zip(measurements, measurements[1:], measurements[2:]):
    sliding.append(sum(map(int, [a, b, c])))
print(len(sliding))
print(sliding)

increases = 0
previous = None
for m in sliding:
    if previous is not None and m > previous:
        increases += 1
    previous = m

print(increases)
