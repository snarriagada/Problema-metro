import sys
 
class Node(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.neighbors = []
        self.previous_node = None
    
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.neighbors.append(self)
            
    def __str__(self):
        return self.name

class Graph(object):
    def __init__(self): 
        self.nodes = [] # self.nodes = [ Node1, Node2, Node3, Node4 ]
        self.train_color = 'green'
        
    def add_node(self, node):
        if node not in self.nodes:
          self.nodes.append(node)
        print('self.nodes modified: ', self.nodes)
        return   

    def value(self, node2):
        "if node2 are the same color as the train or has not color"
        if self.train_color == None: return 1
        if node2.color in [self.train_color, None]:
          return 1  
        else:  
          "if node2 has other color different that the train"
          return 0  

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = graph.nodes
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
    
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    print('shortest path inicial', shortest_path)
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        print("\n")
        print("--> current node now is: ", current_min_node)
        print("\n")        
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = current_min_node.neighbors
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node # podria ser almacenado en el Node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path
  
def print_result(graph, previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    if graph.train_color != None and target_node.color not in [graph.train_color, None]:
        raise Exception("Please confirm that the train can stop in the target station")
        
    while node != start_node:
        if node.color in [graph.train_color, None]: # hace parada en estacion sin color o del mismo que el tren
            path.append(str(node))
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(str(start_node))
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    
a = Node('A', None)
b = Node('B', 'green')
c = Node('C', 'red')
d = Node('D', 'red')
e = Node('E', 'green')
f = Node('F', 'red')
g = Node('G', None)
h = Node('H', 'green')
i = Node('I', None)

a.add_neighbor(b)
b.add_neighbor(c)
c.add_neighbor(d)
d.add_neighbor(i)
d.add_neighbor(h)
h.add_neighbor(i)
g.add_neighbor(h)
g.add_neighbor(b)
g.add_neighbor(f)
e.add_neighbor(f)
a.add_neighbor(e)


graph = Graph()
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)
graph.add_node(e)
graph.add_node(f)
graph.add_node(g)
graph.add_node(h)
graph.add_node(i)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=a)

print_result(graph, previous_nodes, shortest_path, start_node=a, target_node=i)
# EL PRINT RESULT NO DEBE IMPRIMIR LAS ESTACIONES QUE SON COLOR CONTRARIO AL TREN ******



'''
test 1:

a = Node('A', None)
b = Node('B', None)
c = Node('C', None)
d = Node('D', None)
e = Node('E', None)
f = Node('F', None)
g = Node('G', 'green')
h = Node('H', 'red')
i = Node('I', 'green')

a.add_neighbor(b)
b.add_neighbor(c)
c.add_neighbor(d)
c.add_neighbor(g)
d.add_neighbor(e)
e.add_neighbor(f)
f.add_neighbor(i)
i.add_neighbor(h)
h.add_neighbor(g)

graph = Graph()
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)
graph.add_node(e)
graph.add_node(f)
graph.add_node(g)
graph.add_node(h)
graph.add_node(i)




'''