# Advent of Code 2022 - part 3 of N


def day10():
    with open("./inputs/day10", "r") as f:
        data = f.read().splitlines()

    cycle = 0
    X = 1
    signal = []
    for row in data:
        match row.split(" "):
            case ["noop"]:
                cycle += 1
                # print(f"start of {cycle=}")
                # print("do nothing")
                if not (cycle + 20) % 40:
                    signal.append(cycle * X)
                    # print("interesting signal strength!")
                # print(f"end of {cycle=}, {X=}")

            case ["addx", val]:
                val = int(val)

                cycle += 1
                # print(f"start of {cycle=}")
                # print("wait")
                if not (cycle + 20) % 40:
                    signal.append(cycle * X)
                    # print("interesting signal strength!")
                # print(f"end of {cycle=}, {X=}")

                cycle += 1
                # print(f"start of {cycle=}")
                # print("wait")
                if not (cycle + 20) % 40:
                    signal.append(cycle * X)
                    # print("interesting signal strength!")
                X += val
                # print(f"end of {cycle=}. `addx {val}` completed! {X=}")

    return sum(signal)


if __name__ == "__main__":
    for day in range(25):
        try:
            foo = locals()[f"day{day}"]
            print(f"Advent of Code 2022: result for Day {day} is: {foo()}")
        except KeyError:
            pass
