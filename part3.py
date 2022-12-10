# Advent of Code 2022 - part 3 of N


def show_crt(crt):
    for row in crt:
        print("".join(row))


def update_crt(crt, X, cycle):
    x, y = int((cycle - 1) / 40), (cycle - 1) % 40
    if y in [X - 1, X, X + 1]:
        crt[x][y] = "#"


def update_cycle(cycle, X, signal, crt):
    cycle += 1
    if not (cycle + 20) % 40:
        signal.append(cycle * X)
    update_crt(crt, X, cycle)
    return cycle


def day10():
    with open("./inputs/day10", "r") as f:
        data = f.read().splitlines()

    cycle = 0
    X = 1
    signal = []

    crt = [["." for __ in range(40)] for __ in range(6)]

    for d in data:
        match d.split(" "):
            case ["noop"]:
                cycle = update_cycle(cycle, X, signal, crt)

            case ["addx", val]:
                cycle = update_cycle(cycle, X, signal, crt)
                cycle = update_cycle(cycle, X, signal, crt)
                X += int(val)

    show_crt(crt)
    return sum(signal)


if __name__ == "__main__":
    for day in range(25):
        try:
            foo = locals()[f"day{day}"]
            print(f"Advent of Code 2022: result for Day {day} is: {foo()}")
        except KeyError:
            pass
