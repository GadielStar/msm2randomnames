import os
import random
import string

# Ruta al directorio que contiene los archivos .msm
directorio = "msm"

# Itera a través de todos los archivos en el directorio
for filename in os.listdir(directorio):
    # Verifica si el archivo tiene la extensión .msm
    if filename.endswith(".msm"):
        # Genera un nombre aleatorio de 8 caracteres
        nuevo_nombre = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Construye la nueva ruta del archivo con el nombre aleatorio y la extensión .msm
        nueva_ruta = os.path.join(directorio, f"{nuevo_nombre}.msm")
        # Renombra el archivo
        os.rename(os.path.join(directorio, filename), nueva_ruta)
        print(f"Renombrado {filename} a {nuevo_nombre}.msm")

print("thanks for use this unless shit")