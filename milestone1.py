import json
f = open('Input data\level0.json')
data = json.load(f)

for i in data['neighbourhoods']['n0']['distances']:
    print(i)
f.close()
print('Hi!!')


import json
import networkx as nx
from itertools import permutations

def tsp_solver(data):
    # Create a complete graph using distances from the data
    G = nx.Graph()

    for neighborhood in data['neighbourhoods']:
        G.add_node(neighborhood)
        for neighbor, distance in enumerate(data['neighbourhoods'][neighborhood]['distances']):
            G.add_edge(neighborhood, f'n{neighbor}', weight=distance)

    # Solve TSP using permutations
    optimal_path = None
    min_distance = float('inf')

    for perm in permutations(G.nodes()):
        distance = sum(G[perm[i]][perm[i + 1]]['weight'] for i in range(len(perm) - 1))
        distance += G[perm[-1]][perm[0]]['weight']  # Return to the starting point

        if distance < min_distance:
            min_distance = distance
            optimal_path = perm

    return optimal_path, min_distance





data = json.loads(data)


optimal_path, min_distance = tsp_solver(data)


print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
