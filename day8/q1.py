from pathlib import Path


class Try:
    def __init__(self, inputs: str, outputs: str):
        self.inputs = inputs.strip().split(" ")
        self.outputs = outputs.strip().split(" ")


def main(data):

    tries: list[Try] = []
    for line in data.split("\n"):
        inputs, outputs = line.split("|")
        tries.append(Try(inputs, outputs))

    count = 0
    for t in tries:
        # print(f"{t.inputs=}, {t.outputs=}")
        for o in t.outputs:
            if len(o) in [2, 3, 4, 7]:
                count += 1

    print(count)
    return count


assert 26 == main(Path("sample.txt").read_text())
assert 512 == main(Path("data.txt").read_text())
