# Gestion arhicvos
import os
from pathlib import Path

# Crear carpeta
os.makedirs('nueva_carpeta', exist_ok=True)

# Verificar si una ruta existe
ruta = Path('archivo.txt')
print(ruta.exists())

# Obtener nombre del archivo y extensión
print(ruta.stem, ruta.suffix)
