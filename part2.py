# Advent of Code 2022 - part 2 of N


def day7():
    with open("./inputs/day7", "r") as f:
        data = f.read()
    data = data.split("\n")
    data = [d.split() for d in data]

    sizes = dict()
    path = []
    for d in data:
        if d[0] == "$" and d[1] == "cd":
            if d[2] == "..":
                del path[-1]
            else:
                path.append(d[2])
                sizes["\\".join(path)] = 0
        elif (d[0] == "$" and d[1] == "ls") or d[0] == "dir":
            pass
        else:
            for ix in range(len(path)):
                sizes["\\".join(path[: ix + 1])] += int(d[0])

    threshold = 30000000 - (70000000 - sizes["/"])

    return (
        sum(d for d in sizes.values() if d <= 100000),
        min(d for d in sizes.values() if d >= threshold),
    )


if __name__ == "__main__":
    for day in range(25):
        try:
            foo = locals()[f"day{day}"]
            print(f"Advent of Code 2022: result for Day {day} is: {foo()}")
        except KeyError:
            pass
