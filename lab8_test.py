with open("LAB8/input.txt", 'r') as file:
    data = file.read()
    lines = data.splitlines()

#1. Construct the De Bruijin graph
#2. Run Hierholzers Algorithm to find eulerian path
#3. Reconstruct the genome

def construct_debrujin(kmers, k):
    # Initialize empty adjacency list
    graph = {}
    # Iterate over each k-mer
    for kmer in kmers:
        # Extract prefix and suffix
        prefix = kmer[0:k-1]  # First k-1 characters
        suffix = kmer[1:k]   # Last k-1 characters

        # Add edge from prefix to suffix to adjacency list
        graph.setdefault(prefix, []).append(suffix)
    
    # Return adjacency list
    return graph

def nodes_with_outgoing_edges(graph):
    return [node for node, edges in graph.items() if edges]

def copy_graph(graph):
    return {node: edges[:] for node, edges in graph.items()}

def hierholzer(graph, start_node):
    graph_copy = copy_graph(graph)  # Work with a copy of the graph
    stack = []
    eul_path = []
    
    stack.append(start_node)
    
    while stack:
        curr_node = stack[-1]
        untraversed = nodes_with_outgoing_edges(graph_copy)
        
        if curr_node in untraversed:
            next_node = graph_copy[curr_node].pop()
            stack.append(next_node)
        else:
            eul_path.append(stack.pop())
            
    return eul_path[::-1]

def reconstruct(eul_path):
    if not eul_path:
        return ""
    genome = eul_path[0]
    for node in eul_path[1:]:
        genome += node[-1]
    return genome

k = len(lines[0])
graph = construct_debrujin(lines, k)
print(graph)
start_node = next(iter(graph))
eul_path = hierholzer(graph, start_node)
print(eul_path)
new = reconstruct(eul_path)
print(new)


