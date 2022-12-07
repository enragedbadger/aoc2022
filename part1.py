# Advent of Code 2022 - part 1 of N


def day6():
    with open("./inputs/day6", "r") as f:
        data = f.read()

    res = []
    for packet_len in [4, 14]:
        for marker in range(packet_len, len(data)):
            substr = data[marker - packet_len : marker]
            if len(set(substr)) == packet_len:
                res.append(marker)
                break
    return res


def day5():
    crates = {
        1: ["Z", "J", "G"],
        2: ["Q", "L", "R", "P", "W", "F", "V", "C"],
        3: ["F", "P", "M", "C", "L", "G", "R"],
        4: ["L", "F", "B", "W", "P", "H", "M"],
        5: ["G", "C", "F", "S", "V", "Q"],
        6: ["W", "H", "J", "Z", "M", "Q", "T", "L"],
        7: ["H", "F", "S", "B", "V"],
        8: ["F", "J", "Z", "S"],
        9: ["M", "C", "D", "P", "F", "H", "B", "T"],
    }
    with open("./inputs/day5", "r") as f:
        data = f.read()
    data = data.split("\n")

    data = [d.split(" ") for d in data]

    for m in data:
        move = int(m[1])
        fro = int(m[3])
        to = int(m[5])
        # for _ in range(move):
        #     crates[to].extend(crates[fro][-1:])
        #     del crates[fro][-1:]
        crates[to].extend(crates[fro][-move:])
        del crates[fro][-move:]
    return "".join([v[-1] for v in crates.values()])


def day4():
    with open("./inputs/day4", "r") as f:
        data = f.read()
    data = data.split("\n")
    count1 = 0
    count2 = 0
    for row in data:
        elf = row.split(",")
        elf = [e.split("-") for e in elf]
        section = [range(int(e[0]), int(e[1]) + 1) for e in elf]
        section = [list(s) for s in section]
        intersection = [v for v in section[0] if v in section[1]]
        if section[0] == intersection or section[1] == intersection:
            count1 += 1
        if len(intersection) > 0:
            count2 += 1

    return count1, count2


def day3():
    from string import ascii_lowercase

    with open("./inputs/day3", "r") as f:
        data = f.read()
    data = data.split("\n")

    part1 = 0
    for line in data:
        n = int(len(line) / 2)
        c1 = line[:n]
        c2 = line[n:]
        intersection = [v for v in c1 if v in c2][0]
        priority = ord(intersection) - (96 if intersection in ascii_lowercase else 38)
        part1 += priority

    part2 = 0
    for ix in range(0, len(data), 3):
        c = data[ix : ix + 3]
        intersection = [v for v in c[0] if v in c[1]]
        intersection = [v for v in c[2] if v in intersection][0]
        priority = ord(intersection) - (96 if intersection in ascii_lowercase else 38)
        part2 += priority

    return part1, part2


def day2():
    points1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    points2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

    with open("./inputs/day2", "r") as f:
        data = f.read()
    data = data.split("\n")

    res1 = [points1.get(d, 0) for d in data]
    res2 = [points2.get(d, 0) for d in data]
    return sum(res1), sum(res2)


def day1():
    with open("./inputs/day1", "r") as f:
        data = f.read()

    data = [d.split("\n") for d in data.split("\n\n")]
    sums = [sum([int(w) for w in elf]) for elf in data]
    sums.sort()

    return max(sums), sum(sums[-3:])


if __name__ == "__main__":
    for day in range(25):
        try:
            foo = locals()[f"day{day}"]
            print(f"Advent of Code 2022: result for Day {day} is: {foo()}")
        except KeyError:
            pass
