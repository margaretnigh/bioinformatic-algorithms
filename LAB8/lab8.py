from collections import defaultdict, deque

def construct_debrujin(kmers):
    # Initialize empty adjacency list
    graph = defaultdict(deque)
    # Iterate over each k-mer
    for kmer in kmers:
        # Extract prefix and suffix
        prefix = kmer[:-1]  # First k-1 characters
        suffix = kmer[1:]   # Last k-1 characters

        # Add edge from prefix to suffix to adjacency list
        graph[prefix].append(suffix)
    
    # Return adjacency list
    return graph

def find_eulerian_cycle(graph, start_node):
    cycle = []
    stack = [start_node]
    
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].popleft()
            stack.append(next_node)
        else:
            cycle.append(stack.pop())
    
    cycle.reverse()
    return cycle

def assemble_circular_string(cycle, k):
    circular_string = cycle[0]  # Start with the first (k-1)-mer
    for node in cycle[1:]:
        circular_string += node[-1]  # Add the last character of each subsequent (k-1)-mer
    return circular_string

def hierholzer(kmers):
    graph = construct_debrujin(kmers)
    
    # Eulerian cycle
    start_node = kmers[0][:-1]  # Use the prefix of the first k-mer as the start
    cycle = find_eulerian_cycle(graph, start_node)
    
    # circular string
    k = len(kmers[0]) - 1
    circular_string = assemble_circular_string(cycle, k)
    
    # circular string without the last two characters
    return circular_string[:-2]

# Reading input from file
with open("LAB8/input.txt", 'r') as file:
#with open("LAB8/rosalind_grep.txt", 'r') as file:
    data = file.read()
    lines = data.splitlines()

# Assemble the circular sequence
sequence = hierholzer(lines)
print(sequence)
