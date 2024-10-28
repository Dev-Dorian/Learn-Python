usuarios = [[], []]

tamaño = 2

for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificacion = input("Identificación: ")
    
    usuarios[0].append(nombre)
    
    usuarios[1].append(identificacion)
    
for  i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    
    print("Nombre: ", usuarios[0][i])
    print("Identificacion: ", usuarios[1][i])

