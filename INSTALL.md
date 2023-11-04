# Pasos para la instalación del proyecto

## Base de datos

Se encuentra en la carpeta docs el archivo [neptuno.sql](/docs/neptuno.sql) el cual contiene los scripts de la base de datos.

### Contenedor de Base de datos

Entre los archivos principales se encuentra el [docker-compose.yml](/docker-compose.yml), archivo que permitirá generar un contenedor del gestor de base de datos Postgresql para el proyecto, para desplegar este contenedor se debe de realizar los siguientes comandos en la terminal:

```bash
docker-compose up -d
```

Para verificar que el gestor de base de datos está desplegado puede ejecutrar el siguiente comando:

```bash
docker-compose ps
# Resultado
NAME               IMAGE         COMMAND                  SERVICE   CREATED          STATUS          PORTS
pythonbasic-db-1   postgres:13   "docker-entrypoint.s…"   db        45 seconds ago   Up 42 seconds   0.0.0.0:5432->5432/tcp
```

Con lo que se tendrá la base de datos cargada en el gestor configurado en docker.

## Bibliotecas necesarios en el proyecto

Debe instalar los siguientes paquetes para desplegar el proyecto:

```bash
pip install pandas
pip install pymysql

```
