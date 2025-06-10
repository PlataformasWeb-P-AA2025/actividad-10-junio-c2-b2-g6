#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

# Establece el encabezado para indicar que se trata de contenido HTML
print("Content-Type: text/html; charset=UTF-8")  # Especificar UTF-8
print()  # Salto de línea necesario

# Obtención de parámetros a través de CGI (opcional)

# Hace que se pueda recibir datos de un formulario HTML
form = cgi.FieldStorage()
# Obtiene el valor del parámetro 'name' del formulario si no tiene un valor por defecto como 'Invitado'
name = form.getvalue('name', 'Invitado')  # Si no se pasa el parámetro 'name', usa 'Invitado'

# Imprimir el contenido HTML
print(f"""
<html>
<head><title>Ejemplo CGI</title></head>
<body>
    <h1>¡Hola, {name}!</h1>
    <p>Este es un ejemplo básico de un script CGI en Python.</p>
    <form method="GET" action="hello.py">
        <label for="name">Escribe tu nombre: </label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
""")
