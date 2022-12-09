# Advent of Code 2022 - part 2 of N
import numpy as np


def day9():
    with open("./inputs/day9", "r") as f:
        data = f.read().splitlines()

    nav = {
        "U": np.asarray([-1, 0]),
        "D": np.asarray([1, 0]),
        "L": np.asarray([0, -1]),
        "R": np.asarray([0, 1]),
    }
    H = np.asarray([0, 0])
    T = [np.asarray([0, 0])]
    for motion in data:
        direction, size = motion.split()
        for __ in range(int(size)):
            H += nav[direction]
            if np.linalg.norm(H - T[-1]) > 1.5:  # greater than sqrt(2)
                T.append(T[-1] + nav[direction])
                # if after move _still_ diagonal
                if np.isclose(np.linalg.norm(H - T[-1]), np.sqrt(2)):
                    # move again
                    T[-1] = H - nav[direction]
    return len(set(map(tuple, T)))


def day8():
    with open("./inputs/day8", "r") as f:
        data = f.read()

    data = [[int(d) for d in d] for d in data.splitlines()]
    data = np.asarray(data)

    vis = np.ones(data.shape)
    score = np.ones(data.shape)

    for row in range(1, data.shape[0] - 1):
        for col in range(1, data.shape[0] - 1):
            # Left, right, top, bottom - left and top are reversed because we are looking away from (row,col)
            surrounds = [data[row, :col][::-1], data[row, col + 1 :], data[:row, col][::-1], data[row + 1 :, col]]
            max_surrounds = [np.max(s) for s in surrounds]
            vis[row, col] = np.any(max_surrounds < data[row, col])

            for s in surrounds:
                check = s >= data[row, col]
                if not np.any(check):  # All false means we only care about the length of the array
                    score[row, col] *= len(check)
                else:  # Find first instance of a tree as tall or taller - this is why we need reveresed left and top
                    score[row, col] *= np.argmax(check) + 1

    return np.sum(vis), np.max(score)


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
