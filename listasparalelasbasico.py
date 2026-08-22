nombres = []
notas = []

# Carga de datos
for i in range(5): #aca hay un for
    nombre = input("Ingrese el nombre del alumno: ")
    nombres.append(nombre)
    
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

# Mostrar datos
print("\nListado de alumnos:")
for i in range(5):
    print(nombres[i], "-", notas[i])

# Buscar mayor y menor
mayor = notas[0]
menor = notas[0]
pos_mayor = 0
pos_menor = 0

for i in range(1, 5):
    if notas[i] > mayor:
        mayor = notas[i]
        pos_mayor = i
    
    if notas[i] < menor:
        menor = notas[i]
        pos_menor = i

# Resultados
print("\nMayor nota:", nombres[pos_mayor], "-", mayor)
print("Menor nota:", nombres[pos_menor], "-", menor)


