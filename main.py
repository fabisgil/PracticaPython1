import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ingresar_datos():
    nombres = []
    calificaciones = []
    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            notas = input("Ingresa calificaciones separadas por coma: ")
            notas = list(map(float, notas.split(',')))
            nombres.append(nombre)
            calificaciones.append(notas)
        except ValueError:
            print("Error: ingresa solo números separados por coma.")
    return nombres, calificaciones

def crear_dataframe(nombres, calificaciones):
    promedios = [sum(n)/len(n) for n in calificaciones]
    df = pd.DataFrame({
        'Estudiante': nombres,
        'Calificaciones': calificaciones,
        'Promedio': promedios
    })
    return df

def obtener_mejor_estudiante(df):
    mejor = df.loc[df['Promedio'].idxmax()]
    return mejor['Estudiante'], mejor['Promedio']

def guardar_resultados(df, mejor_estudiante, mejor_promedio):
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resultados.txt')
    with open(ruta, 'w') as f:
        for _, fila in df.iterrows():
            f.write(f"{fila['Estudiante']}: {fila['Calificaciones']}, Promedio: {fila['Promedio']:.2f}\n")
        f.write(f"\nMejor estudiante: {mejor_estudiante} con promedio de {mejor_promedio:.2f}\n")
    print(f"Datos guardados en {ruta}")

def graficar_promedios(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Estudiante', y='Promedio', data=df, palette='viridis')
    plt.title('Promedios de Estudiantes')
    plt.ylabel('Promedio')
    plt.xlabel('Estudiante')
    for i, promedio in enumerate(df['Promedio']):
        ax.text(i, promedio + 0.2, f"{promedio:.2f}", ha='center')
    ruta_grafica = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grafica_promedios.png')
    plt.savefig(ruta_grafica)
    plt.close()
    print(f"Gráfica guardada en {ruta_grafica}")

def main():
    nombres, calificaciones = ingresar_datos()
    df = crear_dataframe(nombres, calificaciones)
    mejor_estudiante, mejor_promedio = obtener_mejor_estudiante(df)
    guardar_resultados(df, mejor_estudiante, mejor_promedio)
    graficar_promedios(df)

if __name__ == "__main__":
    main()

