import random

def GibbsSampler(DNA, k, t, N):
    # k: The length of the motifs to find.
    # t: The number of sequences in DNA.
    # N: The number of iterations to run the algorithm.

    # randomly select k-mers Motifs = (Motif1, …, Motif t) in each string from DNA
    Motifs = []
    for i in [random.randint(0, len(DNA[0])-k) for x in range(len(DNA))]:
        j = 0
        kmer = DNA[j][i : k+i]
        j += 1
        Motifs.append(kmer)
    BestMotifs = Motifs
    print(Motifs)
    
    for j in range(1, N):
        i = random.randint(0, t - 1)
        # Profile ← profile matrix constructed from all strings in Motifs except for Motif i
        Profile = profile_matrix(Motifs[:i] + Motifs[i+1:], k, t)
        # Motif[i] ← Profile-randomly generated k-mer in the i-th sequence
        Motifs[i] = kmer_from_profile(DNA[i], k, Profile)
        if score(Motifs, k, t) < score(BestMotifs, k, t):
            BestMotifs = Motifs

    return BestMotifs

def profile_matrix(Motifs, k, t):
    # Initialize the profile matrix with pseudocounts (Laplace smoothing) to avoid zero probabilities
    profile = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}

    for motif in Motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1

    # Convert counts to probabilities
    for nucleotide in 'ACGT':
        profile[nucleotide] = [count / (t + 4) for count in profile[nucleotide]]

    return profile


def kmer_from_profile(sequence, k, Profile):
    n = len(sequence)
    probabilities = []

    # Compute the probability for each k-mer in the sequence
    for i in range(n - k + 1):
        kmer = sequence[i:i + k]
        prob = 1
        for j, nucleotide in enumerate(kmer):
            prob *= Profile[nucleotide][j]
        probabilities.append(prob)

    # Normalize the probabilities
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]

    # Select a k-mer based on the computed probabilities
    cumulative_prob = 0
    r = random.random()
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if r <= cumulative_prob:
            return sequence[i:i + k]
    
    return sequence[-k:]  # In case of rounding issues, return the last k-mer

def score(Motifs, k, t):
    # Initialize a variable to hold the total score
    total_score = 0
    # consensus sequence: for each position in the motifs, determine the most frequent nucleotide (A, C, G, T)
    for motif in Motifs:
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for i in motif:
            if(i == 'A'): counts['A'] += 1
            elif(i == 'C'): counts['C'] += 1
            elif(i == 'G'): counts['G'] += 1
            elif(i == 'T'): counts['T'] += 1
        consensus_nucleotide = max(counts, key=counts.get)
        mismatches = sum(count for nt, count in counts.items() if nt != consensus_nucleotide)
        total_score += mismatches
    return total_score
    
    # score: total number of mismatches between the motifs and the consensus sequence


with open("LAB7/input.txt", 'r') as file:
#with open("LAB7/rosalind_ba2g.txt", 'r') as file:
    data = file.read()
lines = data.splitlines()
motif_length, num_sequences, num_iterations = map(int, lines[0].split())
dna_sequences = lines[1:]

print("Number of Sequences:", num_sequences)
print("Motif Length:", motif_length)
print("Number of Iterations:", num_iterations)
best_motifs = GibbsSampler(dna_sequences, motif_length, num_sequences, num_iterations)
with open("LAB7/output.txt", "w") as file:
    for i in best_motifs:
        print(i)
        file.write(str(i) + " ")