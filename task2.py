import networkx as nx
from collections import deque

metro = nx.Graph()

red_line = [
    "Холодна Гора",              
    "Південний вокзал",         
    "Центральний ринок",
    "Майдан Конституції",
    "Гагаріна",                   
    "Спортивна",
    "Завод імені Малишева",                
    "Турбоатом",
    "Палац Спорту",
    "Армійська",
    "Імені А. С. Масельського",
    "Тракторний завод",
    "Індустріальна"
]
blue_line = [
    "Історичний музей",     
    "Університет",
    "Пушкінська",
    "Київська",
    "Академіка Барабашова",
    "Академіка Павлова",
    "Студентська",
    "Героїв Праці"
]

green_line = [
    "Метробудівників",
    "Захисників України",
    "Архітектора Бекетова",
    "Держпром",
    "Наукова",
    "Ботанічний сад",
    "23 Серпня",
    "Олексіївська",
    "Перемога"                   
]

def add_edges(line):
    for i in range(len(line) - 1):
        metro.add_edge(line[i], line[i+1])

add_edges(red_line)
add_edges(blue_line)
add_edges(green_line)

metro.add_edge("Майдан Конституції", "Історичний музей") 
metro.add_edge("Спортивна", "Захисників України")         
metro.add_edge("Університет", "Держпром")                 


# DFS 
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result
    return None

# BFS 
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        (current, path) = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

start_station = "Холодна Гора"
end_station = "Героїв Праці"

dfs_path = dfs(metro, start_station, end_station)
bfs_path = bfs(metro, start_station, end_station)

print("DFS:")
print(" → ".join(dfs_path))
print("\nBFS:")
print(" → ".join(bfs_path))


print("\nВисновки:")
print(f"DFS пройшов глибше, не обов'язково найкоротшим шляхом ({len(dfs_path)-1} кроків).")
print(f"BFS знайшов шлях з найменшою кількістю пересадок ({len(bfs_path)-1} кроків).")
