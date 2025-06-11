# wandercraft-application/src/day-01, part-02.py
# Code written by Valentin Woehrel, 2025


from part_01 import create_lists


if __name__ == "__main__":
    count = 0

    # create two lists thanks to input file
    list1, list2 = create_lists("input.txt")

    # for each value of list1
    for i in list1:
        # find number of occurence in list2
        occ = list2.count(i)
        # increment the value in counter
        count += i * occ

    print(count)