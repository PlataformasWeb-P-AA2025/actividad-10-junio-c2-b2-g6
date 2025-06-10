import cgi

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    form = cgi.FieldStorage()
    name = form.getvalue('name', 'Invitado')

    # Imprimir el contenido HTML
    return(f"""
    <body>
        <h1>¡Hola, {name}!</h1>
        <p>Este es un ejemplo básico de un script CGI en Python.</p>
        <form method="GET" action="hello.py">
            <label for="name">Escribe tu nombre: </label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Enviar">
        </form>
    </body>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)