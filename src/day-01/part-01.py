# wandercraft-application/src/day-01, part01.py
# Code written by Valentin Woehrel, 2025


from typing import List, Tuple


def create_lists(input_path: str) -> Tuple[List[int], List[int]]:
    """
    Function to create the two lists thanks to the given input file.

    Args:
        input_path: str
            Path to the input file.
    """
    list1 = []
    list2 = []

    # read file
    file = open(input_path)

    # for each line
    for line in file:
        # retrive the two numbers in the line
        first, second = line.split("   ")

        # add numbers in the good lists
        list1.append(int(first))
        list2.append(int(second))

    return (list1, list2)


if __name__ == "__main__":
    count = 0

    # create two lists thanks to input file
    list1, list2 = create_lists("input.txt")

    # sort lists in ascending order
    list1.sort()
    list2.sort()

    # compare difference of each pair
    for i, j in zip(list1, list2):
        # increment counter of the difference
        count += abs(i - j)

    print(count)