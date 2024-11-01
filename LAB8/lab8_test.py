with open("LAB8/example.txt", 'r') as file:
    data = file.read()
    lines = data.splitlines()

#1. Construct the De Bruijin graph
#2. Run Hierholzers Algorithm to find eulerian path
#3. Reconstruct the genome

def construct_debrujin(kmers):
    # Initialize empty adjacency list
    graph = {}
    # Iterate over each k-mer
    for kmer in kmers:
        # Extract prefix and suffix
        prefix = kmer[:-1]  # First k-1 characters
        suffix = kmer[1:]   # Last k-1 characters

        # Add edge from prefix to suffix to adjacency list
        graph.setdefault(prefix, []).append(suffix)
    
    # Return adjacency list
    return graph

def hierholzer(graph):
    # Find the eulerian path
    stack = [] # top of the stack represents current node in path
    eul_path = [] # store final assembly

    # start from any node with outgoing edges since circular DNA
    nodes_with_outgoing_edges = [node for node, edges in graph.items() if edges]
    start_node = nodes_with_outgoing_edges[0]
    stack.append(start_node)
    while stack:
        print("stack: ", stack)
        print("eul_path: ", eul_path)
        print(" ")
        curr_node = stack[-1] # last entry
        # if there is an untraversed edge (if there are edges?)
        if graph.get(curr_node):
            # traverse next edge
            next_node = graph[curr_node].pop()
            stack.append(next_node)
        else:
            # there are no more outgoing edges, complete
            # pop from stack to backtrack and explore other branches
            eul_path.append(stack.pop())
    print("stack: ", stack)
    print("eul_path: ", eul_path)
    return eul_path[::-1]

def reconstruct(eul_path):
    # Start with the first node in the path
    genome = eul_path[0]
    # Add only the last character of each subsequent node to avoid redundancy
    for node in eul_path[1:]:
        genome += node[-1]
    return genome


graph = construct_debrujin(lines)
print(graph)
eul_path = hierholzer(graph)
print(eul_path)
new = reconstruct(eul_path)
print(new)
