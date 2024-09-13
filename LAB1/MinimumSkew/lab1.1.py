#filename = "rosalind_ba1f.txt"
filename = "LAB1/inputs/rosalind_ba1f.txt"

with open(filename, mode="r") as text:
    genome = text.readline().strip("\n")


def SkewArray(genome):
    n = len(genome)
    array = [0] * n
    array[0] = 0
    for i in range(1, n):
        array[i] = array[i-1] + Skew(genome[i-1])
    return array

def Skew(symbol):
    if symbol == 'G':
        return 1
    elif symbol == 'C':
        return -1
    return 0

def MinValue(array):
    return min(array)

def MinimumSkew(genome):
    indices = []
    n = len(genome)
    if n == 0:
        return indices
    array = SkewArray(genome)
    m = MinValue(array)
    for i in range(0, n):
        if array[i] == m:
            indices.append(i)
    return indices


minimumSkew = MinimumSkew(genome)
print(*minimumSkew)