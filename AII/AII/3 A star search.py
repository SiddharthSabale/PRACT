import heapq

import heapq

class Node:
    def __init__(self, state, g=0, h=0):
        self.state = state  # Current state (e.g., a city name)
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost (estimated cost from current node to goal)
        self.f = g + h  # Total estimated cost
        self.parent = None  # Parent node

    def __lt__(self, other):
        return self.f < other.f

def astar_search(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.state == goal.state:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]
        
        closed_set.add(current.state)
        
        for neighbor, cost in graph[current.state].items():
            if neighbor in closed_set:
                continue
            
            g = current.g + cost
            h = heuristic(neighbor, goal.state)  # Assuming a heuristic function is defined
            neighbor_node = Node(neighbor, g, h)
            neighbor_node.parent = current
            
            if any(node.state == neighbor and node.f <= neighbor_node.f for node in open_set):
                continue
            
            heapq.heappush(open_set, neighbor_node)    
    return None

# Example usage:
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic function (assuming a simple straight-line distance heuristic)
def heuristic(node, goal):
    heuristic_values = {
        'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253,
        'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
        'Craiova': 160, 'Rimnicu': 193, 'Fagaras': 178, 'Pitesti': 98,
        'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151,
        'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
    }
    return heuristic_values[node]

# Example usage:
start_node = Node('Arad', 0, heuristic('Arad', 'Bucharest'))
goal_node = Node('Bucharest')

path = astar_search(graph, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found")



