# EJEMPLO 1 RETURN
def sumar(): #Función sin parámetros
    suma = 50 + 10
    return suma #Acá termina la ejecución


print(sumar())

# EJEMPLO 2 CON UN PARAMETRO RETURN
def caracter(n): #Función con un parámetro
    if n == 0: # Usamos el parámetro de la función
        return 'a' # Si n es cero retorna a
        # Notar que de aquí para abajo no se ejecuta nada más

    return 'x' # Este return solo se ejecuta cuando n NO es cero
    
print(caracter(5))

# EJEMPLO 3 CON DOS PARAMETROS RETURN

def mensaje(n, mensaje):
    if(n == 0):
        print(mensaje, n)
        return 1
    return 0

print(mensaje(5, "Hola es el numero"))

# EJEMPLO 4 CON DOS PARAMETROS SIN RETURN

def procedimiento(n, nombre):
    if(n == 0):
        print("hola", nombre)
        return
    print("adiós", nombre)