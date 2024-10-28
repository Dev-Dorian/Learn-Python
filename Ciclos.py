#edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
#for edad in edades:
#    print(edad)

# Recorriendo los índices
#for i in range(len(edades)):
#    print("Por rango", edades[i])
    
#for i in range(len(edades)):
#    print("Prueba por mi ", edades[i])
    
#for ed in edades:
#    print("Otro", ed)
    
numeros = []

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(6)

numeros.pop(1)
numeros.remove(4)

print(numeros)


palabras = ['hola', 'hello', 'heo', 'ola','hello']

palabras.remove('hello')

print(palabras)
# Mostrará ['hola', 'hello', 'ola']

# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])