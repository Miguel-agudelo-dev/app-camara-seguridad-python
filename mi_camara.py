import tkinter as tk
from datetime import datetime

ventana = tk.Tk()
ventana.title("Mi Camara casa")
ventana.geometry("400x500")
ventana.configure(bg="#1e1e1e")

titulo = tk.Label(ventana, text="CÁMARA DE SEGURIDAD", fg="white", bg="#1e1e1e", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

pantalla = tk.Label(ventana, text="[ Aquí se verá tu cámara ]", fg="#00ff00", bg="black", width=40, height=15)
pantalla.pack(pady=10)

def conectar():
    hora = datetime.now().strftime("%H:%M:%S")
    estado.config(text=f"[{hora}] Conectando con cámara V380...", fg="#00ff00")

def tomar_foto():
    hora = datetime.now().strftime("%H:%M:%S")
    estado.config(text=f"[{hora}] ¡Foto guardada!", fg="yellow")

tk.Button(ventana, text="Conectar Cámara", command=conectar, bg="#28a745", fg="white", width=20).pack(pady=5)
tk.Button(ventana, text="Tomar Foto", command=tomar_foto, bg="#007bff", fg="white", width=20).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#dc3545", fg="white", width=20).pack(pady=5)

estado = tk.Label(ventana, text="Sistema listo.", fg="lightgray", bg="#1e1e1e")
estado.pack(pady=10)

ventana.mainloop()
