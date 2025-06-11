# wandercraft-application/src/day-02, part_02.py
# Code written by Valentin Woehrel, 2025


from typing import List
from part_01 import algo


def dampener(rep: List[int]) -> int:
    """
    Check if a report is safe, allowing at most one level to be removed.
    Tries removing each index once and checks if the resulting sequence is safe.

    Args:
        rep: List[int]
            Report to analyse.

    Returns:
        int:
            0: report is unsafe, 1: report is safe
    """
    # report is safe with 0 error
    if algo(rep) == 1:
        return 1

    # error found, try removing each index to check if report is safe
    for i in range(len(rep)):
        modified = rep[:i] + rep[i + 1:]
        if algo(modified):
            return 1

    # report is not safe
    return 0


if __name__ == "__main__":
    count = 0

    with open("input.txt") as file:
        # for each line of the file
        for line in file:
            # create report of the line
            rep = [int(x) for x in line.strip().split()]
            # increment or not counter depending of the result of report analysis
            count += dampener(rep)

    print(count)
