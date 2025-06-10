* Copiar los archivos Dockerfile y hello.py a la carpeta ejemplo-cgi

* Dentro de la carpeta ejecutar en un terminal

  *   docker build -t apache-cgi .
  *   docker run -d -p 8080:80 apache-cgi

* En un navegador ingresar la siguiente dirección

  * http://localhost:8080/cgi-bin/hello.py

* En la wiki, crear una nueva página y explicar que está intentando hacer hello.py, subir una evidencia que el código fue ejecutado de manera exitosa

* Reformular la idea de hello.py, usando un framework MVC como flask, ubicar dicho código en la carpeta ejemplo-flask

* En un nueva hoja de la wiki, subir evidencia y explicar el funcionamiento

