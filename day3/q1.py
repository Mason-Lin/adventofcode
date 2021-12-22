import pprint
from collections import Counter, defaultdict
from pathlib import Path

diagnostic = Path(__file__).parent.joinpath("data.txt").read_text().splitlines()

records = defaultdict(Counter)
for x in diagnostic:
    for i, v in enumerate(x):
        records[i].update(v)
pprint.pprint(records)

pprint.pprint([c.most_common()[0][0] for c in records.values()])
gamma_data = "".join([c.most_common()[0][0] for c in records.values()])
epsilon_data = "".join([c.most_common()[1][0] for c in records.values()])
print(gamma_data, epsilon_data)

epsilon_rate = eval(f"0b{ epsilon_data}")
gamma_rate = eval(f"0b{gamma_data}")
power_consumption = gamma_rate * epsilon_rate
print(gamma_rate, epsilon_rate, power_consumption)
