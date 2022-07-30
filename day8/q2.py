from pathlib import Path
from collections import Counter
from display import SevenSegmentDisplay, get_all_possible_layouts
from filter import Filter

all_possible_layouts: list[SevenSegmentDisplay] = get_all_possible_layouts()


class Try:
    def __init__(self, inputs: str, outputs: str):
        self.inputs = ["".join(sorted(i)) for i in inputs.strip().split(" ")]
        self.outputs = ["".join(sorted(i)) for i in outputs.strip().split(" ")]
        self.combinations = list(set(self.inputs + self.outputs))
        self.mapping = {}

    def get_try_with_specific_length(self, length):
        return [c for c in self.combinations if len(c) == length]

    def get_c1(self):
        return "".join(self.get_try_with_specific_length(2))

    def get_c4(self):
        return "".join(self.get_try_with_specific_length(4))

    def get_c7(self):
        return "".join(self.get_try_with_specific_length(3))

    def get_c8(self):
        return "".join(self.get_try_with_specific_length(7))

    def get_c069(self):
        return "".join(self.get_try_with_specific_length(6))

    def get_c235(self):
        return "".join(self.get_try_with_specific_length(5))

    def get_result(self):
        c1 = self.get_c1()
        c4 = self.get_c4()
        c7 = self.get_c7()
        # c8 = self.get_c8()
        c069 = self.get_c069()
        # c235 = self.get_c235()

        guess = list(set(c4) - set(c1))
        criteria_tl = Filter(lambda x: x.tl == guess[0] and x.mm == guess[1]) | Filter(lambda x: x.tl == guess[1] and x.mm == guess[0])

        tm = (set(c7) - set(c1)).pop()
        criteria_tm = Filter(lambda x, target=tm: x.tm == target)

        for key, count in Counter(c069).items():
            if count == 3:
                continue

            # key is tr, mm, or bl
            if key in c1:
                # key is tr
                criteria_tr = Filter(lambda x, target=key: x.tr == target)
                br = (set(c1) - set(key)).pop()
                criteria_br = Filter(lambda x, target=br: x.br == target)
            elif key in c4:
                # key is mm
                criteria_mm = Filter(lambda x, target=key: x.mm == target)
            else:
                # key is bl
                criteria_bl = Filter(lambda x, target=key: x.bl == target)

        final_criteria = criteria_tl & criteria_tm & criteria_tr & criteria_br & criteria_mm & criteria_bl
        answer = final_criteria.filtered(all_possible_layouts)

        if len(answer) == 1:
            self.answer = answer[0]
            for key in self.combinations:
                self.mapping[key] = self.answer.get_number_by_pattern(key)
            print("PASS")
            return answer
        else:
            print(f"FAIL, still have {len(answer)} answers")
            raise RuntimeError("can not found answer")

    def get_value(self, pattern):
        return self.mapping[pattern]

    def get_total(self):
        total = 0
        for o in self.outputs:
            total *= 10
            value = self.get_value(o)
            total += value
        print(f"{total=}")
        return total


def main(data):
    tries: list[Try] = []
    for line in data.split("\n"):
        inputs, outputs = line.split("|")
        tries.append(Try(inputs, outputs))

    count = 0
    for t in tries:
        # print(f"{t.inputs=}, {t.outputs=} {t.combinations=}")
        t.get_result()
        total = t.get_total()
        count += total
    print(count)
    return count


assert 61229 == main(Path("sample.txt").read_text())
assert 1091165 == main(Path("data.txt").read_text())
