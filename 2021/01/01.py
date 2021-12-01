def part1(lines: list) -> int:
    return len([curr for prev, curr in zip(lines, lines[1:]) if curr > prev])


def part2(lines: list) -> int:
    return len([i for i in range(len(lines) - 3) if lines[i] < lines[i + 3]])


if __name__ == "__main__":
    with open("input", "r") as f:
        puzzle_input = list(map(int, f.readlines()))

    print(part1(puzzle_input))
    print(part2(puzzle_input))
