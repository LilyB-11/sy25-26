F1 =["F1", "VW off-road-bug", 185, (104, 142), 6000, 9, 1880, 4]
E4 =["E4", "Austin Metro 6", 240, (265, 360), 9800, 3.4, 3600, 6]
D3 =["D3", "Seat Toledo Marathon", 220, (195, 330,), 8400, 5.2, 2100, 5]
F2 =["F2", "Mistubishi Galant", 180, (216, 294), 5800, 6.3, 3395, 4]
E1 =["E1", "Mistusbishi Carisma GT", 225, (213, 290), 6000, 5.2, 1996, 4]
G4 =["G4", "Fiat Punto Kit-Car", 165, (165, 220), 7500, 9.8, 1600, 4]
F3 =["F3", "Renault Megane", 218, (198, 270), 8400, 5.9, 1995, 4]
D2 =["D2", "Toyota Celica GT-Four", 245, (220,299), 5600, 5.3, 1998, 4]
E3 =["E3", "Skoda Octavia WRC", 230, (221, 300), 7500, 5.3, 2000, 4]
G2 =["G2", "Seat Ibiza Gti", 220, (205, 280), 8400, 6.5, 1984, 4]
C1 =["C1", "Subaru Impreza WRC", 220, (221, 300), 5500, 5.4, 1994, 4]
G3 =["G3", "Mistubishi Pajero", 185, (153, 208), 7000, 9.6, 3497, 6]

cars = [F1, E4, D3, F2, E1, G4, F3, D2, E3, G2, C1, G3]


top_bottom = "|--------------------------|"
empty_line = "|                          |"
def print_car(c):
    print(top_bottom)
    print(f"|{c[0]}  {c[1]}|")
    print(empty_line)
    print(f"|  speed: {c[2]} 0-60: {c[5]}    |")
    print(empty_line)
    print(f"|  HP: {c[3]} CC: {c[6]} |")
    print(empty_line)
    print(f"|  RPM: {c[4]} cylinders:{c[7]}   |")
    print(empty_line)
    print(top_bottom)
print_car(E1)
for c in cars:
    print_car(c)