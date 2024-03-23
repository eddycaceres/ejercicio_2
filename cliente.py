import socket
import tkinter as tk
from tkinter import Entry, Button, Label

def enviar_cadena():
    host = "127.0.0.1"
    puerto = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, puerto))

    #Obtener la cadena de entrada desde la interfaz gráfica
    data = cadena_input.get()

    #Enviar la cadena de entrada al servidor
    cliente_socket.send(data.encode())

    #Recibir la respuesta del servidor
    respuesta = cliente_socket.recv(1024).decode()

    #Mostrar la respuesta en la interfaz gráfica
    respuesta_label.config(text=respuesta)

    cliente_socket.close()

#Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cliente")
root.geometry("300x150")

#Etiqueta y entrada para la cadena de entrada
cadena_label = Label(root, text="Cadena de entrada:")
cadena_label.pack(pady=5)
cadena_input = Entry(root, width=30)
cadena_input.pack(pady=5)

#Boton para enviar la cadena
boton_enviar = Button(root, text="Enviar", command=enviar_cadena)
boton_enviar.pack(pady=5)

#Etiqueta para mostrar la respuesta del servidor
respuesta_label = Label(root, text="")
respuesta_label.pack(pady=5)

root.mainloop()

