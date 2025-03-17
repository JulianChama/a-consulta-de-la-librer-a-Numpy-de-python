import numpy as np

#  datos aleatorios para los estudiantes
np.random.seed(42)  # F

# Generamos datos ficticios
codigos = np.arange(100000, 106500)  # codigos de estudiantes
nombres = np.array([f"estudiante_{i}" for i in range(6500)])  
carreras = np.random.randint(1, 11, 6500)  # codigo de carrera entre 1 y 10
promedios = np.round(np.random.uniform(2.0, 5.0, 6500), 2)  
años_ingreso = np.random.randint(1980, 2025, 6500)  3

# Introducir codigo de 1 a 10
codigo_carrera = int(input("Ingrese el código de la carrera a listar: "))

# F+filtrar estudiantes con promedio >= 4.0
filtro_carrera = (carreras == codigo_carrera) & (promedios >= 4.0)
estudiantes_destacados = np.column_stack((codigos[filtro_carrera], nombres[filtro_carrera]))

print("\nEstudiantes con promedio >= 4.0 en la carrera", codigo_carrera)
print(estudiantes_destacados)
print("Total de estudiantes destacados:", len(estudiantes_destacados))

# filtrar estudiantes que ingresaron antes de 1990 y están condicionales 
filtro_condicionales = (años_ingreso < 1990) & (promedios < 3.0)
estudiantes_condicionales = np.column_stack((codigos[filtro_condicionales], nombres[filtro_condicionales]))

print("\nestudiantes ingresados antes de 1990 y condicionales:")
print(estudiantes_condicionales)
print("total de estudiantes condicionales:", len(estudiantes_condicionales))
