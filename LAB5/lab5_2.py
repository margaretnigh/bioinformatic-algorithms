with open("LAB5/rosalind_ba5g.txt", "r") as file:
    seq1 = file.readline().strip("\n")
    seq2 = file.readline().strip("\n")

# Represents the minimum number of operations needed to transform one sequence into another
    # Initial State: words we’re transforming
    # Allowed operations:
        # 1. Insertion of a character
        # 2. Removal of a character
        # 3. substitution of a character
        # Goal State: aligned word
        # Path cost: number of edits - what we want to minimize

def print_table(seq1, seq2, table):
    spaced_seq2 = "  ".join(seq2)
    print("      " + spaced_seq2)
    i = 0
    for row in table:
        if i == 0:
            print(" ",row)
            i += 1
        else:
            print(seq1[i-1], row)
            i += 1

def find_edit_distance(x, y):
    n = len(x)
    m = len(y)
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # iterate through each cell in table
    for i in range(1, n+1):
        for j in range(1, m+1):
            # base cases
            table[i][0] = i
            table[0][j] = j
            # recurrance relation
            table[i][j] = min(
                table[i - 1][j] + 1,
                table[i][j - 1] + 1,
                table[i - 1][j - 1] + (0 if x[i - 1] == y[j - 1] else 1)
            )
            # if characters match
            if x[i-1] == y[j-1]:
                # set current cell to diagonal cell
                table[i][j] = table[i-1][j-1]
            # if characters don't match
            else:
                # set current cell to min of left+1, above+1, diagonal+1
                table[i][j] = min(table[i][j-1] + 1, table[i-1][j] + 1, table[i-1][j-1] + 1)
    
    edit_dist = table[n][m]
    print("edit distance: ", edit_dist)

find_edit_distance(seq1, seq2)