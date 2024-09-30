# Define the graph as a dictionary
romania_map = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def dls(graph, start, goal, depth):
    if start == goal:
        return [start]
    if depth <= 0:
        return None
    for neighbor in graph[start]:
        path = dls(graph, neighbor, goal, depth - 1)
        if path:
            return [start] + path
    return None

def iddfs(graph, start, goal):
    depth = 0
    while True:
        path = dls(graph, start, goal, depth)
        if path:
            return path
        depth += 1

# Example usage
start_city = 'Arad'
goal_city = 'Bucharest'
path = iddfs(romania_map, start_city, goal_city)
print(f"Path from {start_city} to {goal_city}: {path}")
