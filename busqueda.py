import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Crear la ventana de la aplicación
root = tk.Tk()
root.withdraw()

# Solicitar al usuario que seleccione la carpeta de búsqueda
print("Seleccione la carpeta de búsqueda")
search_path = filedialog.askdirectory()

# Solicitar al usuario que seleccione la carpeta de destino
print("Seleccione la carpeta de destino")
save_path = filedialog.askdirectory()

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
        shutil.copy(search_path + "/" + file, save_path)
        print("Archivo encontrado: ", file)