from config._config import botbutton  # Importa el decorador para el data de callback
from config.messages.message import gatewaystxtbtn, callbackerrortxt
from config.messages.keyboard import gatewayslistbtn

# Mensaje para el data
@botbutton("gateways")
async def gatewayslist(client, callback_query):
    # Verifica si el usuario que hizo clic en el botón es el mismo que envió el comando
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id

    # Obtén el ID del usuario que envió el comando original
    original_command_message = await client.get_messages(chat_id, callback_query.message.reply_to_message_id)
    command_user_id = original_command_message.from_user.id

    if user_id != command_user_id:
        # Enviar un mensaje de error si el usuario no coincide
        await callback_query.answer(callbackerrortxt, show_alert=True)
    else:
        # Editar el mensaje si el usuario coincide
        await callback_query.edit_message_text(
            text=gatewaystxtbtn.format("t.me/MYKERUIZ"),
            reply_markup=gatewayslistbtn
        )