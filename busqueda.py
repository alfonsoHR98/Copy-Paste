import os
import shutil

# Lectura de pedimentos a buscar
file_names = []
with open("archivos.txt", "r") as file:
  for line in file:
    file_names.append(line.strip())

print("Cantidad de archivos a buscar: ", len(file_names))

# Inserta las terminaciones de los archivos a buscar EJEMPLO: ["PS.pdf","PD.pdf"]
# Ingresa todas las terminaciones que se desean buscar
file_terminals = ["PS.pdf","PD.pdf"]

# Ingresa la ruta de las carpeta donde se desea buscar los archivos
search_path = ""
all_files = os.listdir(search_path)

# Ingresa la ruta de la carpeta donde se desea guardar los archivos encontrados
save_path = ""

# Búsqueda de archivos en la carpeta especificada y guardado en la carpeta especificada
for file_name in file_names:
  for terminal in file_terminals:
    matching_files = list(filter(lambda x: file_name in x and terminal in x, all_files))
    if len(matching_files) > 0:
      for file in matching_files:
        shutil.copy(search_path + "/" + file, save_path)
        print("Archivo encontrado: ", file)