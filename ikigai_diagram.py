import matplotlib.pyplot as plt
from venn import venn

# Definimos los conjuntos para cada área del Ikigai
data = {
    "Lo que amas": {"Naturaleza", "Música", "Cocina"},
    "Lo que el mundo necesita": {"Proyectos ambientales", "Desarrollo comunitario"},
    "Por lo que te pueden pagar": {"Programación", "Análisis de datos", "Emprendimientos"},
    "En lo que eres bueno": {"Creatividad", "Empatía", "Liderazgo"}
}

# Crear el diagrama de Venn
venn(data)

# Añadir el título
plt.title("Diagrama de Ikigai")
plt.show()
