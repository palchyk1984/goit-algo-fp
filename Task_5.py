import uuid
import networkx as nx
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, visit_order, x=0, y=0, layer=1):
    if node in visit_order:
        idx = visit_order.index(node)
        graph.add_node(node.id, color=node.color, label=f"{node.val}\n{idx+1}")
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, visit_order, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, visit_order, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_heap_tree(arr):
    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

def dfs(node, visit_order, depth=0):
    if node is not None:
        node.color = f"#{int(255 - depth * 20):02x}{int(150 + depth * 10):02x}70"
        visit_order.append(node)
        if node.left:
            dfs(node.left, visit_order, depth + 1)
        if node.right:
            dfs(node.right, visit_order, depth + 1)

def bfs(root):
    visit_order = []
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop(0)
        if node is not None:
            node.color = f"#{int(255 - depth * 20):02x}{int(150 + depth * 10):02x}70"
            visit_order.append(node)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return visit_order

def draw_tree(tree_root, visit_order):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos, visit_order)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення і відображення бінарної купи
heap_data = [20, 18, 15, 13, 9, 7, 5, 11, 3, 2]
heap_root = build_heap_tree(heap_data)

# Виконуємо DFS і BFS, потім візуалізуємо
visit_order_dfs = []
dfs(heap_root, visit_order_dfs)
print("DFS order:", [node.val for node in visit_order_dfs])
draw_tree(heap_root, visit_order_dfs)

visit_order_bfs = bfs(heap_root)
print("BFS order:", [node.val for node in visit_order_bfs])
draw_tree(heap_root, visit_order_bfs)
