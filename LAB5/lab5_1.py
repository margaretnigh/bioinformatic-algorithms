# longest common subsequence
with open("LAB5/example3.txt", "r") as file:
    seq1 = file.readline().strip("\n")
    seq2 = file.readline().strip("\n")

print(seq1, seq2)
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
            
def longest_common_substring(x, y):
    # input: strings to be aligned
    # output: longest common subsequence

    n = len(x)
    m = len(y)
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    #print_table(seq1, seq2, table)
    # iterate though each cell in the table
    # 3 paths: from left, above, diagonal
    # because you have to maintain relative ordering
    for i in range(1, n+1):
        for j in range(1, m+1):
            # if char in row-1 == char in col-1
            if x[i-1] == y[j-1]:
                # set cell as diagonal_val + 1
                table[i][j] = 1 + table[i-1][j-1]
            # if above >= left
            elif table[i-1][j] >= table[i][j-1]:
                # set current cell value as above
                table[i][j] = table[i-1][j]
            else: # left > above
                # set current cell value as left
                table[i][j] = table[i][j-1]

    # value in last row and last col of the table
    len_LCS = table[n][m]
    #print_table(seq1, seq2, table)

    # Reconstruct the LCS
    lcs = ""
    i, j = n, m
    # follow path from bottom right of table
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            # prepend character corresponding to each diagonal step in path
            lcs = x[i-1] + lcs
            i -= 1
            j -= 1
        elif table[i-1][j] >= table[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(lcs)
    return lcs

longest_common_substring(seq1, seq2)