# wandercraft-application/src/day-03, part_01.py
# Code written by Valentin Woehrel, 2025


import re


if __name__ == "__main__":
    count = 0
    # define regex pattern: mul(X, Y)
    pattern = r'\bmul\((\d{1,3}),(\d{1,3})\)'

    with open("input.txt") as file:
        content = file.read()

        # find matches with the pattern in the line
        matches = re.findall(pattern, content)

        # increment counter with all mul
        for x, y in matches:
            count += int(x) * int(y)

        print(count)
