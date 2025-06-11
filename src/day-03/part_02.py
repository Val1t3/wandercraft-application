# wandercraft-application/src/day-03, part_02.py
# Code written by Valentin Woehrel, 2025


import re


if __name__ == "__main__":
    count = 0
    # define regex pattern: mul(X, Y), do(), don't()
    pattern = r"\bmul\((\d{1,3}),(\d{1,3})\)|\bdo\(\)|\bdon't\(\)"

    with open("input.txt") as file:
        content = file.read()

    # find matches with the pattern in the file
    # keep the order
    matches = re.finditer(pattern, content)

    # initial state
    enabled = True

    # check for every match
    for match in matches:
        # enable the multiplication
        if match.group(0) == 'do()':
            enabled = True
        # disable the multiplication
        elif match.group(0) == "don't()":
            enabled = False
        # increment to counter the result of the multiplication
        # if state is enabled
        elif enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            count += x * y

    print(count)