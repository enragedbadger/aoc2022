# Advent of Code 2022 - day 11

from dataclasses import dataclass
from math import prod

import yaml


@dataclass
class Monkey:
    monkey_number: int
    items: list
    operation: callable
    operation_val: int
    modulus: int
    true_action: int
    false_action: int
    inspections: int = 0
    global_mod: int = 1

    def inspect(self, monkeys: dict):
        self.inspections += len(self.items)
        self.items = [item % self.global_mod for item in self.items]
        self.items = [
            self.operation([item, item])
            if self.operation_val == "old"
            else self.operation([item, int(self.operation_val)])
            for item in self.items
        ]
        # self.items = [item // 3 for item in self.items]

        for item in self.items:
            if item % self.modulus:
                monkeys[f"Monkey {self.false_action}"].items.append(item)
            else:
                monkeys[f"Monkey {self.true_action}"].items.append(item)

        self.items = []
        return None


def monkey_parser(monkey: str, actions: dict) -> Monkey:
    monkey_number = int(monkey.split(" ")[1])

    if type(actions["Starting items"]) is int:
        items = [actions["Starting items"]]
    else:
        items = list(map(int, actions["Starting items"].split(", ")))

    match actions["Operation"].split(" ")[3]:
        case "*":
            operation = prod
        case "+":
            operation = sum

    operation_val = actions["Operation"].split(" ")[4]
    test_val = int(actions["Test"].split(" ")[2])
    true_action = int(actions["If true"].split(" ")[3])
    false_action = int(actions["If false"].split(" ")[3])
    return Monkey(monkey_number, items, operation, operation_val, test_val, true_action, false_action)


def run(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)

    monkeys = {monkey: monkey_parser(monkey, actions) for monkey, actions in data.items()}

    # All mokeys have prime modulus, so we can combine into a single mega-modulus
    global_mod = prod(m.modulus for m in monkeys.values())
    for m in monkeys.values():
        m.global_mod = global_mod

    for __ in range(10000):
        for m in monkeys.values():
            m.inspect(monkeys)

    return prod(sorted(m.inspections for m in monkeys.values())[-2:])


if __name__ == "__main__":
    print(run("./inputs/day11_test.yml"))
    print(run("./inputs/day11.yml"))
