usuarios = {
    "nombres": [],
    "identificaciones": []
}

tamaño = 2

for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificacion = input("identificacion: ")
    
    usuarios["nombres"].append(nombre)
    
    usuarios["identificaciones"].append(identificacion)
    
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    
    print("Nombre:",usuarios["nombres"][i])
    print("Identificacion:", usuarios["identificaciones"][i])