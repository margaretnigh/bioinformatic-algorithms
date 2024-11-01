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

file_path = "LAB6/sample3.txt"
sequences = read_fasta_from_file(file_path)

s = sequences[0]
t = sequences[1]

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


def globalAlign(X, Y, PAM250, gap_penalty):
    # initialize matrix
    rows, cols = len(X)+1, len(Y)+1
    M = [[0] * cols for _ in range(rows)]
    # initialize first row and column of matrix
    for j in range(1, cols):
        M[0][j] = j * gap_penalty
    for i in range(1, rows):
        M[i][0] = i * gap_penalty
    # follow bellman equation to fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            try:
                #score = BLOSUM62[(X[i-1], Y[j-1])]
                score = PAM250.loc[X[i-1], Y[j-1]]
            except KeyError:
                #score = BLOSUM62[(Y[j-1], X[i-1])]
                score = PAM250.loc[X[i-1], Y[j-1]]
            match = M[i-1][j-1] + int(score)
            delete = M[i-1][j] + gap_penalty
            insert = M[i][j-1] + gap_penalty
            M[i][j] = max(match, delete, insert)
    print_table(X, Y, M)
    return M[rows - 1][cols - 1]

# BLOSUM62 matrix as a dictionary
BLOSUM62 = {
    ('A', 'A'): 4,  ('A', 'C'): 0,  ('A', 'D'): -2, ('A', 'E'): -1, ('A', 'F'): -2, ('A', 'G'): 0,  ('A', 'H'): -2, ('A', 'I'): -1, 
    ('A', 'K'): -1, ('A', 'L'): -1, ('A', 'M'): -1, ('A', 'N'): -2, ('A', 'P'): -1, ('A', 'Q'): -1, ('A', 'R'): -1, ('A', 'S'): 1, 
    ('A', 'T'): 0,  ('A', 'V'): 0,  ('A', 'W'): -3, ('A', 'Y'): -2, ('C', 'C'): 9,  ('C', 'D'): -3, ('C', 'E'): -4, ('C', 'F'): -2, 
    ('C', 'G'): -3, ('C', 'H'): -3, ('C', 'I'): -1, ('C', 'K'): -3, ('C', 'L'): -1, ('C', 'M'): -1, ('C', 'N'): -3, ('C', 'P'): -3, 
    ('C', 'Q'): -3, ('C', 'R'): -3, ('C', 'S'): -1, ('C', 'T'): -1, ('C', 'V'): -1, ('C', 'W'): -2, ('C', 'Y'): -2, ('D', 'D'): 6, 
    ('D', 'E'): 2,  ('D', 'F'): -3, ('D', 'G'): -1, ('D', 'H'): -1, ('D', 'I'): -3, ('D', 'K'): -1, ('D', 'L'): -4, ('D', 'M'): -3, 
    ('D', 'N'): 1,  ('D', 'P'): -1, ('D', 'Q'): 0,  ('D', 'R'): -2, ('D', 'S'): 0,  ('D', 'T'): -1, ('D', 'V'): -3, ('D', 'W'): -4, 
    ('D', 'Y'): -3, ('E', 'E'): 5,  ('E', 'F'): -3, ('E', 'G'): -2, ('E', 'H'): 0,  ('E', 'I'): -3, ('E', 'K'): 1,  ('E', 'L'): -3, 
    ('E', 'M'): -2, ('E', 'N'): 0,  ('E', 'P'): -1, ('E', 'Q'): 2,  ('E', 'R'): 0,  ('E', 'S'): 0,  ('E', 'T'): -1, ('E', 'V'): -2, 
    ('E', 'W'): -3, ('E', 'Y'): -2, ('F', 'F'): 6,  ('F', 'G'): -3, ('F', 'H'): -1, ('F', 'I'): 0,  ('F', 'K'): -3, ('F', 'L'): 0,  
    ('F', 'M'): 0,  ('F', 'N'): -3, ('F', 'P'): -4, ('F', 'Q'): -3, ('F', 'R'): -3, ('F', 'S'): -2, ('F', 'T'): -2, ('F', 'V'): -1, 
    ('F', 'W'): 1,  ('F', 'Y'): 3,  ('G', 'G'): 6,  ('G', 'H'): -2, ('G', 'I'): -4, ('G', 'K'): -2, ('G', 'L'): -4, ('G', 'M'): -3, 
    ('G', 'N'): 0,  ('G', 'P'): -2, ('G', 'Q'): -2, ('G', 'R'): -2, ('G', 'S'): 0,  ('G', 'T'): -2, ('G', 'V'): -3, ('G', 'W'): -2, 
    ('G', 'Y'): -3, ('H', 'H'): 8,  ('H', 'I'): -3, ('H', 'K'): -1, ('H', 'L'): -3, ('H', 'M'): -2, ('H', 'N'): 1,  ('H', 'P'): -2, 
    ('H', 'Q'): 0,  ('H', 'R'): 0,  ('H', 'S'): -1, ('H', 'T'): -2, ('H', 'V'): -3, ('H', 'W'): -2, ('H', 'Y'): 2,  ('I', 'I'): 4,  
    ('I', 'K'): -3, ('I', 'L'): 2,  ('I', 'M'): 1,  ('I', 'N'): -3, ('I', 'P'): -3, ('I', 'Q'): -3, ('I', 'R'): -3, ('I', 'S'): -2, 
    ('I', 'T'): -1, ('I', 'V'): 3,  ('I', 'W'): -3, ('I', 'Y'): -1, ('K', 'K'): 5,  ('K', 'L'): -2, ('K', 'M'): -1, ('K', 'N'): 0,  
    ('K', 'P'): -1, ('K', 'Q'): 1,  ('K', 'R'): 2,  ('K', 'S'): 0,  ('K', 'T'): -1, ('K', 'V'): -2, ('K', 'W'): -3, ('K', 'Y'): -2, 
    ('L', 'L'): 4,  ('L', 'M'): 2,  ('L', 'N'): -3, ('L', 'P'): -3, ('L', 'Q'): -2, ('L', 'R'): -2, ('L', 'S'): -2, ('L', 'T'): -1, 
    ('L', 'V'): 1,  ('L', 'W'): -2, ('L', 'Y'): -1, ('M', 'M'): 5,  ('M', 'N'): -2, ('M', 'P'): -2, ('M', 'Q'): 0,  ('M', 'R'): -1, 
    ('M', 'S'): -1, ('M', 'T'): -1, ('M', 'V'): 1,  ('M', 'W'): -1, ('M', 'Y'): -1, ('N', 'N'): 6,  ('N', 'P'): -2, ('N', 'Q'): 0,  
    ('N', 'R'): 0,  ('N', 'S'): 1,  ('N', 'T'): 0,  ('N', 'V'): -3, ('N', 'W'): -4, ('N', 'Y'): -2, ('P', 'P'): 7,  ('P', 'Q'): -1, 
    ('P', 'R'): -2, ('P', 'S'): -1, ('P', 'T'): -1, ('P', 'V'): -2, ('P', 'W'): -4, ('P', 'Y'): -3, ('Q', 'Q'): 5,  ('Q', 'R'): 1,  
    ('Q', 'S'): 0,  ('Q', 'T'): -1, ('Q', 'V'): -2, ('Q', 'W'): -2, ('Q', 'Y'): -1, ('R', 'R'): 5,  ('R', 'S'): -1, ('R', 'T'): -1, 
    ('R', 'V'): -3, ('R', 'W'): -3, ('R', 'Y'): -2, ('S', 'S'): 4,  ('S', 'T'): 1,  ('S', 'V'): -2, ('S', 'W'): -3, ('S', 'Y'): -2, 
    ('T', 'T'): 5,  ('T', 'V'): 0,  ('T', 'W'): -2, ('T', 'Y'): -2, ('V', 'V'): 4,  ('V', 'W'): -3, ('V', 'Y'): -1, ('W', 'W'): 11, 
    ('W', 'Y'): 2,  ('Y', 'Y'): 7,
}

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

gap_penalty = -5
output = globalAlign(s, t, PAM250, gap_penalty)
with open("LAB6/output.txt", "w") as file:
    file.write(str(output))

