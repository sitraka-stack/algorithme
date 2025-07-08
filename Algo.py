from collections import deque

# Sarintany (carte) amin'ny endrika soratra
sarintany = [
    "SFFFFFF.FFFFFFD",
    "...............",
    "F.F.F.F.F.F.F.F",
    "F..............",
    "F.F.F.F.F.F.F.F",
    "F..............",
    "F.F.F.F.F.F.F.F",
    "F.............E",
    "F.F.F.F.F.F.F.F",
    "F.............."
]

# Haben'ny sarintany
laharana = len(sarintany)
andalana = len(sarintany[0])

# Fikarohana ny toerana 'S' sy 'E'
fiandohana = farany = None
for i in range(laharana):
    for j in range(andalana):
        if sarintany[i][j] == 'S':
            fiandohana = (i, j)
        elif sarintany[i][j] == 'E':
            farany = (i, j)

# Fisaka azo aleha (ambony, ambany, havia, havanana)
fitsipika = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS - fitadiavana lalana fohy indrindra
def bfs_malagasy(fiandohana, farany):
    filaharana = deque([fiandohana])
    efa_nitsidika = set()
    efa_nitsidika.add(fiandohana)
    ray = {}

    while filaharana:
        ankehitriny = filaharana.popleft()
        if ankehitriny == farany:
            break

        for dx, dy in fitsipika:
            ni, nj = ankehitriny[0] + dx, ankehitriny[1] + dy
            if 0 <= ni < laharana and 0 <= nj < andalana and sarintany[ni][nj] != 'F':
                manodidina = (ni, nj)
                if manodidina not in efa_nitsidika:
                    efa_nitsidika.add(manodidina)
                    ray[manodidina] = ankehitriny
                    filaharana.append(manodidina)

    # Fananganana indray ny lalana avy any amin'ny farany
    lalana = []
    ankehitriny = farany
    while ankehitriny != fiandohana:
        lalana.append(ankehitriny)
        ankehitriny = ray.get(ankehitriny)
        if ankehitriny is None:
            return None  # Tsy nisy lalana hita
    lalana.append(fiandohana)
    lalana.reverse()
    return lalana

# Fampisehoana ny vokatra
lalana_voavaha = bfs_malagasy(fiandohana, farany)
if lalana_voavaha:
    for toerana in lalana_voavaha:
        print(toerana)
    print(f"Halavan'ny lalana: {len(lalana_voavaha) - 1}")
else:
    print("Tsy nisy lalana hita")
