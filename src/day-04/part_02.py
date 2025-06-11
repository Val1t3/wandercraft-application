# wandercraft-application/src/day-04, part_02.py
# Code written by Valentin Woehrel, 2025


def check_diag(x: int, y: int, dx: int, dy: int, word: str) -> bool:
    """
    Check if the 3 characters of the word centered at (x, y) in direction
    (dx, dy) from the word "MAS" or "SAM".

    Args:
        x: int
            x position.
        y: int
            y position.
        dx: int
            x direction.
        dy: int
            y direction.

    Returns:
        bool:
            False: word not found, True: word found
    """
    # check diag in every directions
    for i, offset in enumerate([-1, 0, 1]):
        nx = x + dx * offset
        ny = y + dy * offset

        # check boundaries
        if nx < 0 or nx >= len(text[0]) or ny < 0 or ny >= len(text) :
            return False

        # letter not found
        if text[ny][nx] != word[i]:
            return False

    # diagonal found
    return True


if __name__ == "__main__":
    count = 0
    text = []
    words = ["MAS", "SAM"]

    with open("input.txt") as file:
        for line in file:
            text.append(line.strip())

    # get y pos
    for y in range(len(text)):
        # get x pos
        for x in range(len(text[0])):
            # find position where char is 'A'
            if text[y][x] == 'A':
                # define first word
                for w1 in words:
                    # define second word
                    for w2 in words:
                        # check if a diagonal of the two words exists
                        if check_diag(x, y, 1, 1, w1) and check_diag(x, y, -1, 1, w2):
                            # increment counter if yes
                            count += 1

    print(count)
