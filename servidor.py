import socket
import tkinter as tk
from tkinter import messagebox

def procesar_datos(data):
    #Desglosar la cadena de entrada
    codigo_pais = data[:2]
    categoria_edad = data[2:4]
    genero = data[4]
    fecha_nacimiento = data[5:13]
    nombre_completo = data[13:]

    #Validar el codigo de país
    paises = {"01": "Honduras", "02": "Costa Rica", "03": "México", "00": "País Desconocido"}
    if codigo_pais not in paises:
        return "Error: Código de país no válido."

    #Validar la edad
    try:
        categoria_edad = int(categoria_edad)
    except ValueError:
        return "Error: Categoría de edad no válida."

    if categoria_edad <= 18:
        categoria = "menor de edad"
    elif categoria_edad <= 50:
        categoria = "adulto"
    else:
        categoria = "tercera edad"

    #Validar el genero
    if genero not in ["M", "F"]:
        return "Error: Género no válido."

    #Validar la fecha de nacimiento
    try:
        int(fecha_nacimiento)
    except ValueError:
        return "Error: Fecha de nacimiento no válida."

    #Obtener la fecha de nacimiento en formato AAAA-MM-DD
    fecha_nacimiento = f"{fecha_nacimiento[:4]}-{fecha_nacimiento[4:6]}-{fecha_nacimiento[6:]}"

    #Comprobar coherencia entre la edad y la fecha de nacimiento
    if int(fecha_nacimiento[:4]) != 2024 - categoria_edad:
        return f"Error: La edad no concuerda con la fecha de nacimiento."

    #Construccion de la respuesta
    respuesta = f"Hola {nombre_completo.title()}, veo que eres del país de {paises[codigo_pais]} y tienes {categoria_edad} años, lo que indica que eres {'' if genero == 'M' else 'una '} {categoria}."
    respuesta += f" Tu fecha de nacimiento es {fecha_nacimiento}."

    return respuesta

def mostrar_respuesta(respuesta):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Respuesta del servidor", respuesta)
    root.destroy()

def servidor():
    host = "127.0.0.1"
    puerto = 12345

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(1)

    print(f"Servidor escuchando en {host}:{puerto}")

    while True:
        client_socket, addr = servidor_socket.accept()
        print(f"Conexión entrante desde {addr}")

        data = client_socket.recv(1024).decode()
        print(f"Datos recibidos: {data}")

        respuesta = procesar_datos(data)
        print(f"Respuesta: {respuesta}")

        mostrar_respuesta(respuesta)

        client_socket.close()

if __name__ == "__main__":
    servidor()
