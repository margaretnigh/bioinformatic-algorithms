filename = "LAB1/FrequentWords/inputs/rosalind_ba1b.txt"

with open(filename, mode="r") as text:
    textf = text.readline().strip("\n")
    k = int(text.readline().strip("\n"))

def PatternCount(pattern, textf):
    # Slide a window across the text and tally the matches
    count = 0
    n = len(textf)
    k = len(pattern)
    for i in range(0, n-k):
        if textf[i:i+k] == pattern:
            count = count + 1
    return count

def FrequentWords(textf, k):
    # Create two arrays to store the pattern and its associated count
    freqPatterns = []
    n = len(textf)
    count = [0] * (n-k+1)
    # Interate through each pattern in the text and calculate the frequency
    for i in range(0, (n-k+1)):
        pattern = textf[i:i+k]
        count[i] = PatternCount(pattern, textf)
    # Find all most frequent patterns
    maxArr = max(count)
    for i in range(0, n-k):
        if count[i] == maxArr:
            pattern = textf[i:i+k]
            if pattern not in freqPatterns:
                freqPatterns.append(pattern)
    return freqPatterns

frequent_words = FrequentWords(textf, k)
print(*frequent_words)