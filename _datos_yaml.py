import yaml
import logging
import platform
# Otras variables para los formatos de los mensajes 
system_os = platform.system()
punto = "<a href='t.me/NyxChkBot'>•</a>"

# Open Archive datos.yaml :
try:
    with open("config/datos.yaml", "r") as archivo:
        data = yaml.safe_load(archivo)  # Lee el archivo yaml
except FileNotFoundError:
    logging.error("El archivo datos.yaml no se encuentra.")
    exit(1)
except yaml.YAMLError as e:
    logging.error(f"Error al leer el archivo YAML: {e}")
    exit(1)

# Variables Del Bot :
botdata = data.get("bot")
if botdata:
    _api_id = botdata.get("_api_id")
    _api_hash = botdata.get("_api_hash")
    _bot_token = botdata.get("_bot_token")
elif not botdata:
    logging.error("No se encontraron los datos del bot en el archivo YAML.")
    exit(1)
# variables De Datos Del Bot:
botdata = data.get("bot_data")
if botdata:
    version = botdata.get("version")
    last_update = botdata.get("last_update")
    database_type = botdata.get("Database_Type")
elif not botdata:
    logging.error("No se encontraron los datos del bot en el archivo YAML.")
    exit(1)