import os
import shutil

# ruta de la carpeta a buscar
search_path = ""

# ruta de la carpeta donde se guardarán los archivos encontrados
save_path = ""

#Terminaciones de los archivos a buscar
file_terminals = ['PD.pdf', 'PS.pdf']

# Lectura de pedimentos a buscar
file_names = []
with open("archivos.txt", "r") as file:
  for line in file:
    file_names.append(line.strip())

print("Cantidad de archivos a buscar: ", len(file_names))

all_files = os.listdir(search_path)

# Búsqueda de archivos en la carpeta especificada y guardado en la carpeta especificada
for file_name in file_names:
  for terminal in file_terminals:
    matching_files = list(filter(lambda x: file_name in x and terminal in x, all_files))
    if len(matching_files) > 0:
      for file in matching_files:
        shutil.copy(os.path.join(search_path, file), save_path)