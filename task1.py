import networkx as nx
import matplotlib.pyplot as plt

# Граф Харківського метро

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

def add_colored_edges(line, color):
    for i in range(len(line) - 1):
        metro.add_edge(line[i], line[i+1], color=color)

add_colored_edges(red_line, 'red')
add_colored_edges(blue_line, 'blue')
add_colored_edges(green_line, 'green')

metro.add_edge("Майдан Конституції", "Історичний музей")
metro.add_edge("Спортивна", "Метробудівників")
metro.add_edge("Університет", "Держпром")

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(metro, seed=42)

edges = metro.edges(data=True)
edge_colors = [data.get('color', 'black') for _, _, data in edges]


nx.draw(
    metro, pos, with_labels=True, node_size=1400, font_size=9,
    node_color='lightgray', edge_color=edge_colors, width=3
)
plt.title("Харківське метро з кольорами ліній", fontsize=16)
plt.show()


print("Кількість станцій:", metro.number_of_nodes())
print("Кількість з'єднань:", metro.number_of_edges())
print("Ступені станцій (кількість пересадок або сусідніх станцій):")
for station, degree in metro.degree():
    print(f"{station}: {degree}")
