import re

# GOAL: Return the longest substring of s that occurs at least k times in s

filename = "LAB2/example.txt"
with open(filename, "r") as file:
    # Read the entire file content
    file_contents = file.read()

lines = file_contents.split("\n")
genome = lines[0]
genome = genome.replace("$","")
k = int(lines[1])

# A DNA string s (of length at most 20 kbp) with: 
# $ appended, a positive integer k, and a list of edges defining the suffix tree of s
pattern = r"node(\d+) node(\d+) (\d+) (\d+)"
suffix_tree = []

for line in lines[2:-1]:
    match = re.search(pattern, line)
    
    # Each edge is represented by four components:
    parent, child, location, length = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )
    suffix_tree.append([parent, child, location, length])

def PrepareTree(suffix_tree):
    tree = {}
    for edge in suffix_tree:
        parent, child, location, length = edge
        if parent not in tree:
            tree[parent] = []
        tree[parent].append([child, location, length])
    return tree

def CountLeafNodes(node, tree):
    if node not in tree:
        return 1  # It is a leaf
    count = 0
    for child in tree[node]:
        child_node = child[0]
        count += CountLeafNodes(child_node, tree)
    return count

def FindLongestRepeat(suffix_tree, k):
    tree = PrepareTree(suffix_tree)
    max_length = 0
    longest_substring = ""

    for node in tree:
        if node > 1:  # Avoid the root or irrelevant nodes
            leaf_node_count = CountLeafNodes(node, tree)
            
            for child in tree[node]:
                child_node, location, length = child
                if leaf_node_count >= k:
                    substring = genome[location-length-1:location-1]
                    if length > max_length:
                        max_length = length
                        longest_substring = substring

    print("Longest substring that occurs at least", k, "times:", longest_substring)


FindLongestRepeat(suffix_tree, k)
    