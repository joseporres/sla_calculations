En la primera instancia:

Crear la carpeta /var/www

Crear la carpeta /var/nginx

Copiar el archivo nginx.conf en /var/nginx/

Correr el comando

sudo docker run --name minginx   --mount type=bind,source=/var/www,target=/usr/share/nginx/html,readonly    --mount type=bind,source=/var/nginx,target=/etc/nginx    -p 80:80    -d nginx


# Desplegar el api como en la ppt


# Pull del docker de jmeter
```
docker pull justb4/jmeter:latest
```

# Correr el docker de jmeter
```
cd script
sh run_jmeter.sh
```
```
