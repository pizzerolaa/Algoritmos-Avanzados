import sys

def bellman_ford(graph, start, end):
    # Inicializar distancias y padres
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}

    # Relajación de aristas
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    parents[neighbor] = node

    # Verificar ciclos negativos
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("El grafo contiene un ciclo negativo")

    # Reconstruir el camino
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()

    return distances[end], path

# Definir el grafo
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

# Ejecutar el algoritmo
try:
    distance, path = bellman_ford(graph, 'A', 'D')
    print(f"La distancia más corta de A a D es: {distance}")
    print(f"El camino más corto es: {' -> '.join(path)}")
except ValueError as e:
    print(e)

# Imprimir la tabla de iteraciones
def print_iterations(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}

    print("Iteración | Nodo | Distancia | Padre")
    print("-" * 40)

    for i in range(len(graph)):
        print(f"   {i}     |")
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    parents[neighbor] = node
        for node in graph:
            print(f"         |  {node}   |    {distances[node] if distances[node] != float('inf') else '∞'}     |   {parents[node]}")
        print("-" * 40)

print("\nTabla de iteraciones:")
print_iterations(graph, 'A')