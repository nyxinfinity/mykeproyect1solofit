import logging
import os
from pyrogram import Client
from ._function import *

class BotSession:
    def __init__(self, apiid: int = None, apihash: str = None, bottoken: str = None):
        self.api_id = apiid
        self.api_hash = apihash
        self.bot_token = bottoken
        self.logger = Interfaz.setup_logger()  # Configura el logger al inicializar

    def session(self):
        # Crea el cliente y lo guarda en bot
        bot = Client(
            name="nyx",
            api_id=self.api_id,
            api_hash=self.api_hash,
            bot_token=self.bot_token,
            plugins=dict(root="src"),
            device_model="Bot",
            app_version="0.1",
            lang_code="es"
        )
        if bot:
            print("\033[92mBot: On \033[0m\n")
            print("\033[33mInformación: El bot se está configurando.\033[0m \n")
            # Realiza cualquier otra configuración necesaria
            return bot
        else:
            self.logger.error("Verifica tus datos, no se configuró el cliente")

class Interfaz(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[96m',  # Cyan
        'INFO': '\033[36m',   # Cyan
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[97m\033[41m',  # White with Red Background
        'RESET': '\033[0m',  # Reset color
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        reset = self.COLORS['RESET']
        return f"{color}{super().format(record)}{reset}"

    @staticmethod
    def setup_logger():
        # Configuración del logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Configura el nivel de log general
        formatter = Interfaz("[%(levelname)s] %(message)s")
        if not logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    @staticmethod
    def clean():
        # Limpia la pantalla según el sistema
        if os.name == 'posix':
            os.system('clear')  # Comando para sistemas tipo Unix (Linux y macOS)
        elif os.name == 'nt':
            os.system('cls')  # Comando para Windows
        else:
            print("\033c", end="")  # Alternativa para otros sistemas (ANSI escape code)
            
    @staticmethod
    def title():
      text = """
    _____        __ _       _ _           ____   ____ _______ 
   |_   _|      / _(_)     (_) |         |  _ \ / __ \__   __|
     | |  _ __ | |_ _ _ __  _| |_ _   _  | |_) | |  | | | |   
     | | | '_ \|  _| | '_ \| | __| | | | |  _ <| |  | | | |   
    _| |_| | | |  | | | | | | | |_| |_| | | |_) | |__| | | |   
   |_____|_| |_|_| |_|_| |_|_|\__|\__, | |____/ \____/  |_|   
                                   __/ |                      
                                  |___/                       
  """
      print(f"\033[94m{text}\033[0m")