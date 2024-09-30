from collections import deque
import sys

infinity = float('inf')

class Node:
    def _init_(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def _repr_(self):
        return "<Node{}>".format(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state,
                                           action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def _eq_(self, other):
        return isinstance(other, Node) and self.state == other.state

    def _hash_(self):
        return hash(self.state)

class Graph:
    def _init_(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for b, dist in self.graph_dict[a].items():
                self.connect(b, a, dist)

    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, A, B=None):
        links = self.graph_dict.setdefault(A, {})
        if B is None:
            return links
        else:
            return links.get(B)

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    @classmethod
    def UndirectedGraph(cls, graph_dict=None):
        return cls(graph_dict=graph_dict, directed=False)

class Problem(object):
    def _init_(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return state in self.goal
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError

class GraphProblem(Problem):
    def _init_(self, initial, goal, graph):
        super()._init_(initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or infinity)

    def find_min_edge(self):
        m = infinity
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)
        return m

    @staticmethod
    def depth_limited_search(node, problem, limit=50):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = GraphProblem.depth_limited_search(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    @staticmethod
    def iterative_deepening_search(problem, limit):
        for depth in range(0, limit + 1):
            print("checking with depth:", depth)
            result = GraphProblem.depth_limited_search(Node(problem.initial), problem, depth)
            print("result:", result)
            if result and result != 'cutoff':
                return result
        return None

if __name__ == "_main_":
    romania_map = Graph.UndirectedGraph(dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75,),
        Eforie=dict(Hirsova=86,),
        Hirsova=dict(Urziceni=98,),
        Iasi=dict(Vaslui=92, Neamt=87,),
        Lugoj=dict(Timisoara=111, Mehadia=70,),
        Oradea=dict(Zerind=71, Sibiu=151,),
        Pitesti=dict(Rimnicu=97,),
        Rimnicu=dict(Sibiu=80,),
        Urziceni=dict(Vaslui=142,)
    ))

    print("Searching from Arad to Bucharest with level 5...")
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    print(GraphProblem.iterative_deepening_search(romania_problem, 5))

    print("\nSearching from Arad to Bucharest with level 2...")
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    print(GraphProblem.iterative_deepening_search(romania_problem, 2))