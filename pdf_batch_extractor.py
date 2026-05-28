import csv
import shutil
import os

# Ruta del CSV
csv_file = "input_files.csv"

# Carpeta origen (donde están los PDFs)
origen = r"C:\Users\Aleja\Downloads"

# Carpeta destino (donde quedaran los PDFs)
destino = "output"

# Creara una carpeta destino en caso de que no exista
os.makedirs(destino, exist_ok=True)

with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

# Limpiar nombres de columnas
    reader.fieldnames = [field.strip().replace('\ufeff', '') for field in reader.fieldnames]
    for row in reader:
        nombre = row["nombre"]
        archivo_origen = os.path.join(origen, f"{nombre}.pdf")
        archivo_destino = os.path.join(destino, f"{nombre}.pdf")

        if os.path.exists(archivo_origen):
            shutil.copy(archivo_origen, archivo_destino)
            print(f"✅ Copiado: {nombre}.pdf")
        else:
            print(f"❌ No encontrado: {nombre}.pdf")