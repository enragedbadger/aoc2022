# Advent of Code 2022 - day 21

from scipy.optimize import fsolve


def data():
    with open("./inputs/day21", "r") as f:
        data = f.read().splitlines()
    return data


def test_data():
    data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".splitlines()
    return data


class Monkey:
    OPERATION = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    def __init__(self, name: str, value: int = None, source1: str = None, source2: str = None, operation: str = None):
        self.name = name
        if value:  # this "base" monkey shouts a number
            self._value = value
            self.base = True
        else:
            self._value = None
            self.source1_name = source1
            self.source2_name = source2
            self.operation_name = operation
            self.base = False

            self.source1 = None
            self.source2 = None
            self.operation = self.OPERATION[self.operation_name]

    def __repr__(self):
        if self.base:
            return f"Monkey: {self.name}, {self.value}"
        else:
            return f"Monkey: {self.name}, {self.source1_name} {self.operation_name} {self.source2_name} = {self.value}"

    @property
    def value(self):
        if self.base:
            return self._value
        else:
            return self.operation(self.source1.value, self.source2.value)

    @value.setter
    def value(self, val):
        if self.base:
            self._value = val
        else:
            pass

    @staticmethod
    def link(monkeys):
        for m in monkeys.values():
            if not m.base:
                m.source1 = monkeys[m.source1_name]
                m.source2 = monkeys[m.source2_name]

    @staticmethod
    def load(data):
        monkeys = {}
        for d in data:
            match d.split():
                case [name, value]:
                    monkeys[name[:-1]] = Monkey(name=name[:-1], value=int(value))

                case [name, source1, op, source2]:
                    monkeys[name[:-1]] = Monkey(name=name[:-1], source1=source1, source2=source2, operation=op)
        return monkeys


def run(data):
    monkeys = Monkey.load(data)
    Monkey.link(monkeys)
    part1 = int(monkeys["root"].value)

    root = fsolve(f, 1e12, args=monkeys)
    monkeys["humn"].value = root[0]
    return part1, int(root)


def f(x, monkeys):
    monkeys["humn"].value = x[0]
    s1 = monkeys["root"].source1_name
    s2 = monkeys["root"].source2_name
    print(f"humn={x[0]}, source1={monkeys[s1].value}, source2={monkeys[s2].value}")
    return monkeys[s1].value - monkeys[s2].value


if __name__ == "__main__":
    print(run(data()))
