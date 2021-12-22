from collections import Counter
from pathlib import Path

diagnostic = Path(__file__).parent.joinpath("data.txt").read_text().splitlines()
length = len(diagnostic[0])


def get_rate(rule):
    pre = ""
    bit_criteria = 0
    check = None
    while check != 1:
        filtered = [x for x in diagnostic if x.startswith(pre)]
        bit_of_filtered = [list(x)[bit_criteria] for x in filtered]
        counter = Counter(bit_of_filtered).most_common()
        bit_criteria += 1

        more, more_count = counter[0]

        if len(counter) == 2:
            fewer, fewer_count = counter[1]
            if more_count == fewer_count:
                more = "1" if rule == "more" else "0"
        # FIXME fewer
        pre += more if rule == "more" else fewer
        unique_data = [x for x in diagnostic if x.startswith(pre)].pop()
        check = more_count if rule == "more" else fewer_count
    rate = eval(f"0b{unique_data}")
    print("found", unique_data, rate)
    return rate


oxygen_rate = get_rate("more")
co2_rate = get_rate("less")
life_support_rating = co2_rate * oxygen_rate
print(life_support_rating)

assert life_support_rating == 4996233
