import numpy as np

# Datos base
np.random.seed(42)  # Fijamos la semilla para obtener los mismos valores siempre
total_estudiantes = 6500

# Generar códigos de estudiantes (simples números consecutivos)
codigos = np.arange(100000, 100000 + total_estudiantes)

# Simulación de nombres (usaremos "Estudiante_XXX" con su código)
nombres = np.array([f"Estudiante_{codigo}" for codigo in codigos])

# Generar promedios aleatorios entre 2.0 y 5.0
promedios = np.random.uniform(2.0, 5.0, total_estudiantes)

# Generar códigos de carrera (aleatorio entre 1 y 10)
carreras = np.random.randint(1, 11, total_estudiantes)

# Generar años de ingreso (aleatorio entre 1980 y 2023)
años_ingreso = np.random.randint(1980, 2024, total_estudiantes)

# Generar estados (0 = Normal, 1 = Condicional)
estados = np.random.randint(0, 2, total_estudiantes)  

# ---------- FILTRO 1: Estudiantes de carrera X con promedio >= 4 ----------
codigo_carrera = int(input("Ingrese el código de la carrera a listar: "))

# Filtramos estudiantes de la carrera X con promedio >= 4
filtro1 = (carreras == codigo_carrera) & (promedios >= 4.0)

# Mostramos los estudiantes que cumplen con la condición
print("\nEstudiantes con promedio >= 4 en la carrera", codigo_carrera)
contador1 = 0
for i in range(total_estudiantes):
    if filtro1[i]:  
        print(f"{codigos[i]} - {nombres[i]}")
        contador1 += 1
print(f"Total encontrados: {contador1}")

# ---------- FILTRO 2: Estudiantes ingresados antes de 1990 y condicionales ----------
filtro2 = (años_ingreso < 1990) & (estados == 1)

print("\nEstudiantes ingresados antes de 1990 y condicionales:")
contador2 = 0
for i in range(total_estudiantes):
    if filtro2[i]:  
        print(f"{codigos[i]} - {nombres[i]}")
        contador2 += 1
print(f"Total encontrados: {contador2}")
