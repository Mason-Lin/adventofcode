from pathlib import Path

measurements = Path("data").read_text().splitlines()

print(len(measurements))
# measurements = [1,2,3,2,1,2,1,0,5,8,7,5,6000,5,7]
increases = 0
previous = None
for m in measurements:
    if previous is not None and m > previous:
        increases += 1
    previous = m

print(increases)
