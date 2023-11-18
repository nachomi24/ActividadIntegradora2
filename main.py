#Situacion Problema 2
#Optimizacion de un sistema de tuberías de agua potable

#----------Librerias----------#
import matplotlib.pyplot as plt
import numpy as np

#----------Problema 1----------#
class Node:
    def __init__(self, id, x, y, is_source):
        self.id = id
        self.x = x
        self.y = y
        self.is_source = is_source

class Edge:
    def __init__(self, node1, node2, diameter):
        self.node1 = node1
        self.node2 = node2
        self.diameter = diameter

def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_nodes, num_edges = map(int, lines[0].split())
        nodes = []
        edges = []
        office = None
        new_nodes = []
        mode = None
        for line in lines[1:]:
            if line.startswith("[NODES]"):
                mode = "nodes"
                continue
            elif line.startswith("[EDGES]"):
                mode = "edges"
                continue
            elif line.startswith("[OFFICE]"):
                mode = "office"
                continue
            elif line.startswith("[NEW]"):
                mode = "new"
                continue
            if mode == "nodes":
                id, x, y, is_source = line.split()
                nodes.append(Node(id, float(x), float(y), int(is_source)))
            elif mode == "edges":
                node1, node2, diameter = line.split()
                edges.append(Edge(node1, node2, int(diameter)))
            elif mode == "office":
                office = line.strip()
            elif mode == "new":
                x, y, diameter = line.split()
                new_nodes.append((float(x), float(y), int(diameter)))

        return nodes, edges, office, new_nodes

def print_graph(nodes, edges, office, new_nodes):
    print("Nodes:")
    for node in nodes:
        print(f"ID: {node.id}, X: {node.x}, Y: {node.y}, Is Source: {node.is_source}")
    print("\nEdges:")
    for edge in edges:
        print(f"Node 1: {edge.node1}, Node 2: {edge.node2}, Diameter: {edge.diameter}")
    print(f"\nOffice: {office}")
    print("\nNew Nodes:")
    for new_node in new_nodes:
        print(f"X: {new_node[0]}, Y: {new_node[1]}, Diameter: {new_node[2]}")

nodes, edges, office, new_nodes = read_graph('HAN.txt')
print_graph(nodes, edges, office, new_nodes)


#----------Problema 2----------#
# Calcula la longitud de una tubería
def calculate_length(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

# Crea un diccionario de nodos para facilitar la búsqueda por id
nodes_dict = {node.id: node for node in nodes}

# Crea el gráfico
plt.figure(figsize=(10, 6))

# Dibuja los nodos
for node in nodes:
    plt.scatter(node.x, node.y, color='blue')
    plt.text(node.x, node.y, node.id, fontsize=12, ha='right')

# Dibuja las tuberías y calcula sus longitudes
for edge in edges:
    node1 = nodes_dict[edge.node1]
    node2 = nodes_dict[edge.node2]
    plt.plot([node1.x, node2.x], [node1.y, node2.y], color='black')
    length = calculate_length(node1, node2)
    mid_x = (node1.x + node2.x) / 2
    mid_y = (node1.y + node2.y) / 2
    plt.text(mid_x, mid_y, f'{length:.2f}', fontsize=10, ha='center')

plt.title('Red de distribución de agua')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.show()
