from functools import lru_cache
from itertools import permutations


class SevenSegmentDisplay:
    def __init__(self, tm: str, tl: str, tr: str, mm: str, bl: str, br: str, bm: str):
        self.tm: str = tm
        self.tl: str = tl
        self.tr: str = tr
        self.mm: str = mm
        self.bm: str = bm
        self.bl: str = bl
        self.br: str = br

    def __repr__(self):
        new_str = []
        for str_tmp in self.positions():
            new_str.append(str_tmp.format(**self.__dict__))
        return "\n".join(new_str)

    def positions(self):
        positions = [
            " --{tm}--",
            "|     |",
            "{tl}     {tr}",
            "|     |",
            " --{mm}--",
            "|     |",
            "{bl}     {br}",
            "|     |",
            " --{bm}--",
        ]
        return positions

    def get_number(self, num):
        assert 0 <= num <= 9
        return {
            0: sorted(f"{self.tm}{self.tl}{self.tr}{self.bm}{self.bl}{self.br}"),
            1: sorted(f"{self.tr}{self.br}"),
            2: sorted(f"{self.tm}{self.tr}{self.mm}{self.bm}{self.bl}"),
            3: sorted(f"{self.tm}{self.tr}{self.mm}{self.bm}{self.br}"),
            4: sorted(f"{self.tl}{self.tr}{self.mm}{self.br}"),
            5: sorted(f"{self.tm}{self.tl}{self.mm}{self.bm}{self.br}"),
            6: sorted(f"{self.tm}{self.tl}{self.mm}{self.bm}{self.bl}{self.br}"),
            7: sorted(f"{self.tr}{self.br}"),
            8: sorted(f"{self.tm}{self.tl}{self.tr}{self.mm}{self.bm}{self.bl}{self.br}"),
            9: sorted(f"{self.tm}{self.tl}{self.tr}{self.mm}{self.bm}{self.br}"),
        }[num]


@lru_cache
def get_all_possible_layouts():
    return [SevenSegmentDisplay(*i) for i in permutations("abcdefg", 7)]
