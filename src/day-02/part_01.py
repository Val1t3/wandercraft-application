# wandercraft-application/src/day-02, part_01.py
# Code written by Valentin Woehrel, 2025


from typing import List


def algo(rep: List[int]) -> int:
    """
    Function who contains the report analysis by checking rules.

    Args:
        rep: List[int]
            Report to analyse.

    Returns:
        int:
            0: report is unsafe, 1: report is safe
    """
    # detect increase or decrease mode
    increase = rep[0] < rep[1]

    # check if report is safe or unsafe by checking rules
    for i in range(len(rep) - 1):
        a, b = rep[i], rep[i + 1]

        # check direction consistency rules
        if (increase and a >= b) or (not increase and a <= b):
            return 0

        # check difference rules
        if abs(a - b) < 1 or abs(a - b) > 3:
            return 0

    # report is safe
    return 1


if __name__ == "__main__":
    count = 0

    with open("input.txt") as file:
        # for each line of the file
        for line in file:
            # create report of the line
            rep = [int(x) for x in line.split()]
            # increment or not counter depending of the result of report analysis
            count += algo(rep)

    print(count)
