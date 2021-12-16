from pathlib import Path

measurements = Path("data").read_text().splitlines()

print(len(measurements))
# measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
increases = 1
previous = None
for m in measurements:
    if previous is not None and m > previous:
        increases += 1
    previous = m

print(increases)
