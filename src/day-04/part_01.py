# wandercraft-application/src/day-04, part_01.py
# Code written by Valentin Woehrel, 2025


def check_around(x: int, y: int, dx: int, dy: int) -> int:
    word = "XMAS"

    # check if every letter appears
    for i in range(4):
        nx = x + dx * i
        ny = y + dy * i

        # check boundaries
        if ny < 0 or ny >= len(text) or nx < 0 or nx >= len(text[0]):
            return 0

        # letter not found
        if text[ny][nx] != word[i]:
            return 0

    # XMAS has been found
    return 1


if __name__ == "__main__":
    count = 0
    text = []
    directions = [
        (1, 0),    # right
        (1, 1),    # down-right
        (0, 1),    # down
        (-1, 1),   # down-left
        (-1, 0),   # left
        (-1, -1),  # up-left
        (0, -1),   # up
        (1, -1),   # up-right
    ]

    with open("input.txt") as file:
        for line in file:
            text.append(line.strip())

    # get y pos
    for y in range(len(text)):
        # get x pos
        for x in range(len(text[0])):
            # check in every direction if we can find the word "XMAS"
            for dx, dy in directions:
                # increment counter if word is found
                count += check_around(x, y, dx, dy)

    print(count)
