import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        pq = [(0, src)]  # Бінарна купа, ініціалізована початковою вершиною

        while pq:
            (cur_dist, cur_vertex) = heapq.heappop(pq)

            # Якщо поточна відстань вже більша ніж знайдена, пропускаємо ітерацію
            if cur_dist > dist[cur_vertex]:
                continue

            for neighbor, weight in self.graph[cur_vertex]:
                distance = cur_dist + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return dist

# Приклад використання
graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 8, 2)
graph.add_edge(2, 5, 4)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(6, 8, 6)
graph.add_edge(7, 8, 7)

distances = graph.dijkstra(0)
print("Відстань від вершини 0 до інших:")
for i in range(len(distances)):
    print(f"До вершини {i} = {distances[i]}")
