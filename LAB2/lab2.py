import re

# GOAL: Return the longest substring of s that occurs at least k times in s

filename = "LAB2/example.txt"
with open(filename, "r") as file:
    # Read the entire file content
    file_contents = file.read()

lines = file_contents.split("\n")
genome = lines[0]
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

def FindLongestRepeat(tree, k, genome):
    suffix_tree = PrepareTree(tree)
    for children in suffix_tree:
        # for each internal node count the number of leaf nodes in its subtree
        for node in suffix_tree[children]:
            child, location, length = node
    # this count tells you how many times the substring corresponding to that internal node appears in the string
    # if # of leaf nodes is at least k, substring is valid candidate for the longest multiple repeat
        # while traversing, keep track of the longest substring that has at least k occurances to find the answer
def CountLeafNodes(node):
    if node not in suffix_tree:
        return 1  # it is a leaf node
    return sum(count_leaf_nodes(child) for child in suffix_tree[node])

FindLongestRepeat(suffix_tree, k, genome) 
    