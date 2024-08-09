import random  # Para elegir de manera random las imagenes
from config._config import botcmd
from config.messages.message import starttxt, photos_array
from config.messages.keyboard import startbutton
from _datos_yaml import system_os, punto,version, last_update, database_type
# Comando Start, Star
@botcmd(["start", "star"])
async def startcmd(client, msg):
    await client.send_photo(
        chat_id=msg.chat.id,
        photo=random.choice(photos_array),
        caption=starttxt.format(
            msg.from_user.mention,
            punto,  # Placeholder para punto
            version,
            punto,
            system_os,
            punto,
            last_update,
            punto,
            "Python 3.12", # Lenguaje
            punto,
            database_type
        ),
        reply_to_message_id=msg.id,
        reply_markup=startbutton
    )