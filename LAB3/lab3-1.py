with open("LAB3/rosalind_ba9j.txt", "r") as file:
    # Read the entire file content
    bwt = file.read()

def reverse_bwt(bwt):
    # list of (character, index) tuples
    char_index = [(char, i) for i, char in enumerate(bwt)]
    
    # sort the list
    sorted_char_index = sorted(char_index)
    
    # create the transformation table
    table = [0] * len(bwt)
    for i, (char, index) in enumerate(sorted_char_index):
        table[index] = i
    
    # reconstruct the original string
    result = []
    next_index = table[0]
    for _ in range(len(bwt) - 1):
        result.append(sorted_char_index[next_index][0])
        next_index = table[next_index]
    og_str = ''.join(result)[::-1]
    og_str = og_str + '$'
    return og_str

# Test the function
original = reverse_bwt(bwt)
print(original.replace('\n', ''))
with open("LAB3/output.txt", "w") as file:
    file.write(original.replace('\n', ''))