import json 
from sys import maxsize
import networkx as nx
from itertools import permutations

def optimal_path(data):
    
    path = nx.Graph()

    for neighborhood in data['neighbourhoods']:

        path.add_node(neighborhood) 

        for neighbor, distance in enumerate(data['neighbourhoods']['n0']['distances']):
            path.add_edge(neighborhood, f'n{neighbor}', weight=distance)
            print("Neigh:",neighbor)
            print("Dist:",distance)
        
    min_path = maxsize
    optimal_path = None
    min_distance = float('inf')

    for perm in permutations(path.nodes()):
        distance = sum(path[perm[i]][perm[i + 1]]['weight'] for i in range(len(perm) - 1))
        distance += path[perm[-1]][perm[0]]['weight']       

        if distance < min_distance:
            min_distance = distance
            optimal_path = perm

    return optimal_path, min_distance


f = open('Input data\level0.json')
data = json.load(f)

#print(data)
optimal_path, min_distance = optimal_path(data)
print(optimal_path)