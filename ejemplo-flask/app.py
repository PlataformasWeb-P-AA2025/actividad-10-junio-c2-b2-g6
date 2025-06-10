from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Invitado')

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo en Flask</title>
    </head>
    <body>
        <h1>¡Hola, {name}!</h1>
        <p>Este es un ejemplo básico de una aplicación Flask.</p>
        <form method="GET" action="/">
            <label for="name">Escribe tu nombre: </label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)