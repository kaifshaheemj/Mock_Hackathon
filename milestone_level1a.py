import json
import itertools

def create_distance_matrix(data):
    num_neighborhoods = data['n_neighbourhoods']
    distance_matrix = [[0] * num_neighborhoods for _ in range(num_neighborhoods)]

    for i in range(num_neighborhoods):
        for j in range(num_neighborhoods):
            distance_matrix[i][j] = data['neighbourhoods'][f'n{i}']['distances'][j]

    return distance_matrix

def find_optimized_slots(distance, res_dist, ord_quantities, max_cap):
    node_order = sorted(range(len(res_dist)), key=lambda x: res_dist[x])
    slots = []
    current_slot = []
    current_capacity = 0
    current_distance = 0

    for node in node_order:
        if current_capacity + ord_quantities[node] <= max_cap:
            current_slot.append(node)
            current_capacity += ord_quantities[node]
            print(current_slot)
            print(current_capacity)
            if len(current_slot) > 1:
                current_distance += distance[current_slot[-2]][current_slot[-1]]
        else:
            slots.append((current_slot, current_distance))
            current_slot = [node]
            current_capacity = ord_quantities[node]
            current_distance = 0

    if current_slot:
        slots.append((current_slot, current_distance))
    print("slots:",slots)
    optimized_slots = []

    for slot, _ in slots:
        possible_orders = itertools.permutations(slot)
        min_distance = float('inf')
        best_order = []

        for order in possible_orders:
            dist = sum(distance[order[i]][order[i+1]] for i in range(len(order) - 1))
            if dist < min_distance:
                min_distance = dist
                best_order = order

        optimized_slots.append((best_order, min_distance))

    return optimized_slots

f = open('Input data\level1a.json')
data = json.load(f)
distance_matrix = create_distance_matrix(data)

neighbour=data['neighbourhoods']
capacity = data['vehicles']['v0']['capacity']
order_quantities = [data['neighbourhoods'][f'n{i}']['order_quantity'] for i in range(20)]
restaurant_distance = data['restaurants']['r0']['neighbourhood_distance']

print('capacity',capacity)
print('ordered_quantities:', order_quantities)
print('restaurant dist:', restaurant_distance)
print("Order_quantity for each area ",order_quantities)
print("Distance to neighbourhood from restaurant r0 :",restaurant_distance)
print("capacity of scooter :",capacity)
print("Total quantity :",sum(order_quantities))
print("minimum number of Trips :",round(sum(order_quantities)/capacity))

os = find_optimized_slots(distance_matrix, restaurant_distance, order_quantities, capacity)
final_lst=[]
for i in os:
    temp=[]
    temp.append('r0')
    for j in i[0]:
        temp.append('n'+str(j))
    temp.append('r0')
    final_lst.append(temp)

final_slots={"v0": {"path1": final_lst[0], "path2": final_lst[1], "path3": final_lst[2],"path4":final_lst[3]}}
print(final_slots)

save_file = open("level1a_output.json", "w")  
json.dump(final_slots, save_file, indent = 6)  
save_file.close()
