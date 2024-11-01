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

from copy import deepcopy

def find_all_eulerian_circuits(graph):
    all_circuits = []
    def hierholzer(curr_graph, stack, eul_path):
        curr_node = stack[-1]
        if curr_graph.get(curr_node):
            print("stack: ", stack)
            print("eul_path: ", eul_path)
            print(" ")
            for next_node in curr_graph[curr_node][:]:  # Copy to avoid in-loop modifications
                # Create a new graph with the edge removed
                next_graph = deepcopy(curr_graph)
                next_graph[curr_node].remove(next_node)
                stack.append(next_node)
                hierholzer(next_graph, stack, eul_path)
                stack.pop()  # backtrack
            else:
                # If circular and path is valid, store it
                if len(eul_path) == sum(len(edges) for edges in graph.values()) + 1:
                    all_circuits.append(eul_path + [curr_node])
    
    # Start DFS from each node with outgoing edges
    nodes_with_outgoing_edges = [node for node in graph if graph[node]]
    for start_node in nodes_with_outgoing_edges:
        hierholzer(deepcopy(graph), [start_node], [])
    
    return all_circuits

def reconstruct(eul_path):
    # Start with the first node in the path
    genome = eul_path[0]
    # Add only the last character of each subsequent node to avoid redundancy
    for node in eul_path[1:]:
        genome += node[-1]
    return genome


graph = construct_debrujin(lines)
print(graph)
eul_path = find_all_eulerian_circuits(graph)
print(eul_path)
new = reconstruct(eul_path)
print(new)
