import json

def create_distance_matrix(data):
    num_neighborhoods = data['n_neighbourhoods']
    distance_matrix = [[0] * num_neighborhoods for _ in range(num_neighborhoods)]

    for i in range(num_neighborhoods):
        for j in range(num_neighborhoods):
            distance_matrix[i][j] = data['neighbourhoods'][f'n{i}']['distances'][j]

    return distance_matrix

def optimized_path(distance_matrix, restaurant_distances, order_quantities, max_capacity):
    current_capacity = 0
    current_quantity = 0
    current_distance = 0
    path = []

    for node in sorted(range(len(restaurant_distances)), key=lambda x: restaurant_distances[x]):
        if current_capacity + order_quantities[node] <= max_capacity:
            current_capacity += order_quantities[node]
            current_quantity += order_quantities[node]
            if path:
                print(path)
                current_distance += distance_matrix[path[-1]][node]
                print(distance_matrix[path[-1]][node])
            path.append(node)

    return path, current_quantity, current_distance

with open('Input data\\level1a.json') as f:
    data = json.load(f)

distance_matrix = create_distance_matrix(data)

capacity = data['vehicles']['v0']['capacity']
order_quantities = [data['neighbourhoods'][f'n{i}']['order_quantity'] for i in range(20)]
restaurant_distance = data['restaurants']['r0']['neighbourhood_distance']
optimal_path, max_quantity, total_distance = optimized_path(distance_matrix, restaurant_distance, order_quantities, capacity)
print("Optimized Path:", optimal_path)
print("Max Quantity Delivered:", max_quantity)
print("Total Distance Traveled:", total_distance)
