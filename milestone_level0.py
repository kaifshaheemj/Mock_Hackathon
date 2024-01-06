import json
from itertools import permutations
from sys import maxsize

def create_distance_matrix(data):
    num_neighborhoods = data['n_neighbourhoods']
    distance_matrix = [[0] * num_neighborhoods for _ in range(num_neighborhoods)]

    for i in range(num_neighborhoods):
        for j in range(num_neighborhoods):
            distance_matrix[i][j] = data['neighbourhoods'][f'n{i}']['distances'][j]

    return distance_matrix

def tsp_solver(graph, start_node):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    print("Num Node", num_nodes)
    path = [start_node]
    total_cost = 0

    while len(path) <= num_nodes:
        current_node = path[-1]
        min_cost = float('inf')
        next_node = None

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] < min_cost:
                min_cost = graph[current_node][neighbor]
                next_node = neighbor

        if next_node is not None:
            path.append(next_node)
            visited[next_node] = True
            total_cost += min_cost

    # Return to the starting node
    print(start_node)
    path.append(start_node)

    total_cost += graph[path[-2]][start_node]

    return path, total_cost

with open('Input data\\level0.json') as f:
    data = json.load(f)

distance_matrix = create_distance_matrix(data)
print("Distance mat:",distance_matrix)
start_node = data['restaurants']['r0']['restaurant_distance'][0] 
print(start_node)
optimal_path, min_distance = tsp_solver(distance_matrix, start_node)
print(len(optimal_path))
#optimal_path = {"v0" : {"path" : optimal_path}}
optimal_path = json.dumps(optimal_path)
print(type(optimal_path))
print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
output_file_path = "level0_output_16.json"
output_data = {
    "v0": {"path": optimal_path}
}
with open(output_file_path, 'w') as json_file:
    json.dump(output_data, json_file)

opt_path = ['r0','n0','n11','n4','n15','n10','n14','n17','n7','n19','n6','n5','n12','n9','n2','n18','n1','n16','n3','n13','n8','r0']
print(opt_path)
print(len(opt_path))

output_file_path = "level0_output.json"
output_data = {
    "v0": {"path": opt_path}
}
with open(output_file_path, 'w') as json_file:
    json.dump(output_data, json_file)