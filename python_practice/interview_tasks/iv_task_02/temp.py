graph = g = [
    {'A': 1},
    {'B': ['A' + 'C']},
    {'C': ['A' + 'D']},
    {'D': ['A']},
    {'E': ['A' + 'D']},
    {'F': ['B' + 'G']},
    {'G': ['C']},
    {'H': ['D' + 'G']},
    {'I': ['E']},
    {'J': ['F' + 'G' + 'H' + 'I']}
]
print(g[9]['J'])
