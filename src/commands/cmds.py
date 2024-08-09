import random  # Para elegir de manera random las imágenes
from config._config import botcmd  # Importa el decorador de comandos
from config.messages.message import cmdstxt, photos_array  # Importa las fotos y mensajes
from config.messages.keyboard import comandsbutton  # Importa los botones para start

# Comando Start, Star
@botcmd(["cmd", "cmds", "help", "comandos", "comando", "ayuda"])
async def cmds_cmd(client, msg):
    # Enviar el mensaje con la foto y los botones en línea
    await client.send_photo(
        chat_id=msg.chat.id,
        photo=random.choice(photos_array),
        caption=cmdstxt,
        reply_to_message_id=msg.id,
        reply_markup=comandsbutton
    )