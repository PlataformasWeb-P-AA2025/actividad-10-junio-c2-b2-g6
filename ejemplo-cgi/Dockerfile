# Usar la imagen base de Apache con soporte CGI
FROM httpd:2.4

# Instalar Python 3 (ya está incluido en las imágenes modernas de Debian)
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

# Habilitar el soporte CGI en Apache y configurar el directorio adecuado
RUN echo "LoadModule cgi_module modules/mod_cgi.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "ScriptAlias /cgi-bin/ /usr/local/apache2/cgi-bin/" >> /usr/local/apache2/conf/httpd.conf && \
    echo "<Directory \"/usr/local/apache2/cgi-bin\">" >> /usr/local/apache2/conf/httpd.conf && \
    echo "    Options +ExecCGI" >> /usr/local/apache2/conf/httpd.conf && \
    echo "    AddHandler cgi-script .py .cgi" >> /usr/local/apache2/conf/httpd.conf && \
    echo "    Require all granted" >> /usr/local/apache2/conf/httpd.conf && \
    echo "</Directory>" >> /usr/local/apache2/conf/httpd.conf

# Copiar el script CGI al directorio adecuado
COPY hello.py /usr/local/apache2/cgi-bin/hello.py

# Cambiar permisos para que el script sea ejecutable
RUN chmod +x /usr/local/apache2/cgi-bin/hello.py

# Exponer el puerto 80 para acceder al servidor
EXPOSE 80

# Iniciar Apache
CMD ["httpd-foreground"]
