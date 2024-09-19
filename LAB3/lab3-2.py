with open("rosalind_ba9m.txt", "r") as file:
    bwt = file.readline().strip("\n")
    patterns = file.readline().strip("\n").split(" ")


def BetterBWTPatternMatch(bwt, str):
    n = len(bwt)
    # set inital indices
    top = 0
    bottom  = n - 1
    bwt_sorted = sort(bwt)

    while top is less than bottom:
        if str not empty:
            char == str[-1]
            remove char from str
            if char in bwt[top:bottom]:
                top = bwt_sorted index of char in range
                bottom = bwt_sorted index of last char in range
            else no match
        else return bottom - top + 1 to get number of matches