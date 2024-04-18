mi_tabla = [['Dorian','Carlos'],[21, 23]]

# Recorriendo los elementos

# Accedemos a cada fila (que es una lista)

for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)

# Recorriendo los índices
# i serían las filas
for i in range(len(mi_tabla)):
    for j in range(len(mi_tabla[i])):
        print(mi_tabla[i][j])
        
fila = 0

# Con while y los índices
while fila < len(mi_tabla):
    columna = 0
    while columna < len(mi_tabla[fila]):
        print(mi_tabla[fila][columna])
        columna += 1
    fila += 1