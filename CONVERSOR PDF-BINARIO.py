import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import base64
import os

def pdf_a_binario(pdf, archivo_binario):
    with open(pdf, "rb") as pdf_file:
        contenido_binario = pdf_file.read()
    with open(archivo_binario, "wb") as binario_file:
        binario_file.write(contenido_binario)

def binario_a_pdf(archivo_binario, ruta_destino_pdf):
    with open(archivo_binario, "rb") as binario_file:
        contenido_binario = binario_file.read()
    with open(ruta_destino_pdf, "wb") as pdf_file:
        pdf_file.write(contenido_binario)

def abrir_explorador_pdf():
    archivo_seleccionado = filedialog.askopenfilename(title="Seleccionar archivo PDF", filetypes=[("Archivos PDF", "*.pdf")])
    if archivo_seleccionado:
        pdf_original_entry.delete(0, tk.END)
        pdf_original_entry.insert(0, archivo_seleccionado)

def abrir_explorador_binario():
    archivo_seleccionado = filedialog.askopenfilename(title="Seleccionar archivo binario", filetypes=[("Archivos binarios", "*.bin")])
    if archivo_seleccionado:
        ruta_binario_entry.delete(0, tk.END)
        ruta_binario_entry.insert(0, archivo_seleccionado)

def abrir_explorador_destino_binario():
    ubicacion_guardado = filedialog.askdirectory(title="Seleccionar carpeta para guardar archivo binario")
    if ubicacion_guardado:
        ruta_destino_binario_entry.delete(0, tk.END)
        ruta_destino_binario_entry.insert(0, ubicacion_guardado)

def abrir_explorador_destino_pdf():
    ubicacion_guardado = filedialog.askdirectory(title="Seleccionar carpeta para guardar archivo PDF")
    if ubicacion_guardado:
        ruta_destino_pdf_entry.delete(0, tk.END)
        ruta_destino_pdf_entry.insert(0, ubicacion_guardado)

def convertir_pdf_binario():
    pdf_original = pdf_original_entry.get()
    ruta_destino_binario = ruta_destino_binario_entry.get()
    pdf_a_binario(pdf_original, os.path.join(ruta_destino_binario, "archivo.bin"))
    resultado_label.config(text=f"El archivo PDF se ha convertido a binario y se ha guardado en {ruta_destino_binario}.")

def convertir_binario_pdf():
    ruta_binario = ruta_binario_entry.get()
    ruta_destino_pdf = ruta_destino_pdf_entry.get()
    binario_a_pdf(ruta_binario, os.path.join(ruta_destino_pdf, "archivo.pdf"))
    resultado_label.config(text=f"El archivo binario se ha convertido a PDF y se ha guardado en {ruta_destino_pdf}.")

# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.title("Convertidor PDF - Binario")

# Crear dos frames para dividir la ventana en dos secciones
frame_izquierdo = ttk.Frame(ventana)
frame_derecho = ttk.Frame(ventana)
frame_izquierdo.pack(side="left", padx=10, pady=10)
frame_derecho.pack(side="right", padx=10, pady=10)

# Crear campos de entrada y etiquetas para la conversión de PDF a binario
pdf_original_label = ttk.Label(frame_izquierdo, text="Ruta del archivo PDF original:")
pdf_original_entry = ttk.Entry(frame_izquierdo)
ruta_destino_binario_label = ttk.Label(frame_izquierdo, text="Carpeta donde se guardará el archivo binario:")
ruta_destino_binario_entry = ttk.Entry(frame_izquierdo)

# Botones para abrir el explorador de archivos para la conversión de PDF a binario
seleccionar_pdf_button = ttk.Button(frame_izquierdo, text="Seleccionar PDF", command=abrir_explorador_pdf)
seleccionar_destino_binario_button = ttk.Button(frame_izquierdo, text="Seleccionar Destino Binario", command=abrir_explorador_destino_binario)

# Botones para realizar la conversión de PDF a binario
convertir_pdf_binario_button = ttk.Button(frame_izquierdo, text="Convertir PDF a Binario", command=convertir_pdf_binario)

# Etiqueta para mostrar el resultado de la conversión de PDF a binario
resultado_label = ttk.Label(frame_izquierdo, text="")

# Colocar widgets en el frame izquierdo
pdf_original_label.grid(row=0, column=0, sticky="w")
pdf_original_entry.grid(row=0, column=1, padx=5, pady=5)
seleccionar_pdf_button.grid(row=0, column=2, padx=5, pady=5)
ruta_destino_binario_label.grid(row=1, column=0, sticky="w")
ruta_destino_binario_entry.grid(row=1, column=1, padx=5, pady=5)
seleccionar_destino_binario_button.grid(row=1, column=2, padx=5, pady=5)
convertir_pdf_binario_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
resultado_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Crear campos de entrada y etiquetas para la conversión de binario a PDF
ruta_binario_label = ttk.Label(frame_derecho, text="Ruta del archivo binario:")
ruta_binario_entry = ttk.Entry(frame_derecho)
ruta_destino_pdf_label = ttk.Label(frame_derecho, text="Carpeta donde se guardará el archivo PDF:")
ruta_destino_pdf_entry = ttk.Entry(frame_derecho)

# Botones para abrir el explorador de archivos para la conversión de binario a PDF
seleccionar_binario_button = ttk.Button(frame_derecho, text="Seleccionar Binario", command=abrir_explorador_binario)
seleccionar_destino_pdf_button = ttk.Button(frame_derecho, text="Seleccionar Destino PDF", command=abrir_explorador_destino_pdf)

# Botones para realizar la conversión de binario a PDF
convertir_binario_pdf_button = ttk.Button(frame_derecho, text="Convertir Binario a PDF", command=convertir_binario_pdf)

# Etiqueta para mostrar el resultado de la conversión de binario a PDF
resultado_label2 = ttk.Label(frame_derecho, text="")

# Colocar widgets en el frame derecho
ruta_binario_label.grid(row=0, column=0, sticky="w")
ruta_binario_entry.grid(row=0, column=1, padx=5, pady=5)
seleccionar_binario_button.grid(row=0, column=2, padx=5, pady=5)
ruta_destino_pdf_label.grid(row=1, column=0, sticky="w")
ruta_destino_pdf_entry.grid(row=1, column=1, padx=5, pady=5)
seleccionar_destino_pdf_button.grid(row=1, column=2, padx=5, pady=5)
convertir_binario_pdf_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
resultado_label2.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Iniciar la aplicación
ventana.mainloop()
