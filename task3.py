import networkx as nx
import matplotlib.pyplot as plt

metro = nx.Graph()

def add_line(edges, color):
    for u, v, weight in edges:
        metro.add_edge(u, v, weight=weight, color=color)

red_edges = [
    ("Холодна Гора", "Південний вокзал", 2),
    ("Південний вокзал", "Центральний ринок", 3),
    ("Центральний ринок", "Майдан Конституції", 3),
    ("Майдан Конституції", "Наукова", 2),
    ("Наукова", "Гагаріна", 2),
    ("Гагаріна", "Спортивна", 2),
    ("Спортивна", "Завод імені Малишева", 2),
    ("Завод імені Малишева", "Турбоатом", 3),
    ("Турбоатом", "Палац Спорту", 2),
    ("Палац Спорту", "Армійська", 3),
    ("Армійська", "Імені А. С. Масельського", 2),
    ("Імені А. С. Масельського", "Тракторний завод", 3),
    ( "Тракторний завод", 'Індустріальна', 3)
]
add_line(red_edges, "red")

blue_edges = [
    ("Героїв Праці", "Студентська", 3),
    ("Студентська", "Академіка Павлова", 3),
    ("Академіка Павлова", "Академіка Барабашова", 3),
    ("Академіка Барабашова", "Київська", 3),
    ("Київська", "Пушкінська", 3),
    ("Пушкінська", "Університет", 3),
    ("Університет", "Історичний музей", 3)
]
add_line(blue_edges, "blue")

green_edges = [
    ("Перемога", "Олексіївська", 3),
    ("Олексіївська", "23 Серпня", 2),
    ("23 Серпня", "Ботанічний сад", 2),
    ("Ботанічний сад", "Наукова", 2),
    ("Наукова", "Держпром", 3),
    ("Держпром", "Архітектора Бекетова", 3),
    ("Архітектора Бекетова", "Захисників України", 3),
    ("Захисників України", "Метробудівників", 2)
]
add_line(green_edges, "green")


transfer_edges = [
    ("Майдан Конституції", "Історичний музей", 0.5),
    ("Університет", "Держпром", 0.5),  
    ("Спортивна", "Захисників України", 0.5) 
]

add_line(transfer_edges, "black")

pos = nx.spring_layout(metro, seed=42)
plt.figure(figsize=(14, 10))
edge_colors = [data['color'] for _, _, data in metro.edges(data=True)]
edge_labels = nx.get_edge_attributes(metro, 'weight')

nx.draw(
    metro, pos, with_labels=True, node_size=1400,
    node_color='lightgray', edge_color=edge_colors, width=3, font_size=9
)
nx.draw_networkx_edge_labels(metro, pos, edge_labels=edge_labels)
plt.title("Харківське метро — з вагами та кольорами ліній", fontsize=16)
plt.show()

# Алгоритм Дейкстри
print("Найкоротші відстані між всіма станціями метро (алгоритм Дейкстри):\n")

for source in metro.nodes():
    lengths, paths = nx.single_source_dijkstra(metro, source=source, weight='weight')
    print(f"З {source}:")
    for target in metro.nodes():
        if source != target:
            print(f"  -> до {target}: відстань = {lengths[target]}, шлях = {paths[target]}")
    print()