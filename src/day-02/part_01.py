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
    increase = True
    if rep[0] > rep[1]:
        increase = False

    # check if report is safe or unsafe by checking rules
    for index, item in enumerate(rep[:-1]):
        next_item = rep[index+1]

        # checking rules
        if increase and item > next_item:
            return 0
        elif not increase and item < next_item:
            return 0
        elif abs(item - next_item) < 1:
            return 0
        elif abs(item - next_item) > 3:
            return 0

    # report is safe
    return 1


if __name__ == "__main__":
    count = 0

    file = open("input.txt")

    # for each line of the file
    for line in file:
        # create report of the line
        rep = [int(x) for x in line.split(" ")]
        # increment or not counter depending of the result of report analysis
        count += algo(rep)

    print(count)