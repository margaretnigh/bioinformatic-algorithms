def read_fasta_from_file(file_path):
    sequences = []
    current_sequence = ""
    
    with open(file_path, 'r') as fasta_file:
        for line in fasta_file:
            if line.startswith(">"):  # Skip headers
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line.strip()
        
        # Append the last sequence
        if current_sequence:
            sequences.append(current_sequence)
    
    return sequences

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

file_path = "LAB6/rosalind_loca.txt"
sequences = read_fasta_from_file(file_path)

s = sequences[0]
t = sequences[1]

def localAlign(X, Y, PAM250, gap_penalty):
    # initialize matrix
    rows, cols = len(X)+1, len(Y)+1
    M = [[0] * cols for _ in range(rows)]

    max_score = 0
    # follow bellman equation to fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            score = PAM250.loc[X[i-1], Y[j-1]]
            match = M[i-1][j-1] + int(score)
            delete = M[i-1][j] + gap_penalty
            insert = M[i][j-1] + gap_penalty
            M[i][j] = max(0, match, delete, insert)
            if M[i][j] > max_score:
                max_score = M[i][j]
                max_score_location = (i,j)
    #print_table(X, Y, M)
    alignX, alignY = backtracking(M, X, Y, max_score_location)
    newX = alignX[::-1]
    newY = alignY[::-1]
    #print(newX, newY)
    with open("LAB6/output.txt", "w") as file:
        file.write(str(max_score) + "\n")
        file.write(str(newX) + "\n")
        file.write(str(newY))
    return (newX, newY)

def backtracking(M, X, Y, max_score_location):
    alignX = ""
    alignY = ""
    i, j = max_score_location

    while M[i][j] != 0:
        if X[i-1] == Y[j-1]:
            alignX += X[i-1]
            alignY += Y[j-1]
            i -= 1
            j -= 1
        else:
            directions = [M[i-1][j-1], M[i-1][j], M[i][j-1]]
            # Find the maximum score among the neighbors
            # Determine the direction based on the maximum score
            if max(directions) == directions[0]:
                alignX += X[i-1]
                alignY += Y[j-1]
                i -= 1
                j -= 1
            elif max(directions) == directions[1]:
                alignX += X[i-1]
                #alignY += ""
                i -= 1
            elif max(directions) == directions[-1]:
                #alignX += ""
                alignY += Y[j-1]
                j -= 1
            else:
                break

    return alignX, alignY


gap_penalty = -5
import pandas as pd
with open("LAB6/PAM250.txt", 'r') as file:
    data = file.read()

lines = data.splitlines()
table_data = [line.split() for line in lines]
header = table_data[0]
header.insert(0, " ")
row_labels = [row[0] for row in table_data[1:]]
matrix_values = [row[1:] for row in table_data[1:]]
PAM250 = pd.DataFrame(matrix_values, columns=header[1:], index=row_labels)
result = localAlign(s, t, PAM250, gap_penalty)
print(result)