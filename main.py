import logging
from config._config import BotSession, Interfaz
from _datos_yaml import _api_id, _api_hash, _bot_token

if not _api_id or not _api_hash or not _bot_token:
    logging.error("Faltan datos de configuración del bot en el archivo YAML.")
    exit(1)

# Inicio del bot y manejo de interrupciones
def main():
    Interfaz.clean()  # Limpia la pantalla antes de iniciar el bot
    try:
        Interfaz.title()
        bot = BotSession(apiid=_api_id, apihash=_api_hash, bottoken=_bot_token)
        session = bot.session()
        session.run()  # Corre la sesión
        Interfaz.clean()  # Limpia la pantalla después de que el bot se apague
        print("\033[91mBot: Off \033[0m")
    except Exception as e:
        logging.error(f"Error al iniciar el bot: {e}")
        exit(1)

if __name__ == "__main__":
    main()