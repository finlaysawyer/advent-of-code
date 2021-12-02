def part1(lines: list) -> int:
    pos = depth = 0

    for command, value in lines:
        value = int(value)
        match command:
            case "forward":
                pos += value
            case "down":
                depth += value
            case "up":
                depth -= value

    return pos * depth


def part2(lines: list) -> int:
    pos = depth = aim = 0

    for command, value in lines:
        value = int(value)
        match command:
            case "forward":
                pos += value
                depth += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value

    return pos * depth


if __name__ == "__main__":
    with open("input", "r") as f:
        puzzle_input = [i.strip('\n').split(" ") for i in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
