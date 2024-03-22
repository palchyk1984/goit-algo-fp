import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def add_edges(graph, node, pos, visit_order, x=0, y=0, layer=1):
    if node in visit_order:
        idx = visit_order.index(node)
        graph.add_node(node.val, color=calculate_color(idx, len(visit_order)), label=f"{node.val}\n{idx+1}")
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            add_edges(graph, node.left, pos, visit_order, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            add_edges(graph, node.right, pos, visit_order, x=r, y=y - 1, layer=layer + 1)
    return graph

def calculate_color(index, total):
    r = 0.1 + 0.9 * (index / total)
    g = 0.1
    b = 0.9 - 0.9 * (index / total)
    return (r, g, b, 1.0)

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
            visit_order.append(node)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    return visit_order

def draw_tree(tree_root, visit_order):
    tree = nx.DiGraph()
    pos = {node.val: (0, -i) for i, node in enumerate(visit_order)}
    tree = add_edges(tree, tree_root, pos, visit_order)

    colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

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
