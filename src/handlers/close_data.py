import asyncio  # Para usar asyncio.sleep
from config._config import botbutton  # Importa el decorador para el data de callback
from config.messages.message import end_callbackbtn, callbackerrortxt

# Mensaje para el data
@botbutton("finbtn")
async def finfinbtn(client, callback_query):
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
        # Eliminar el mensaje del bot y el original del usuario
        await client.delete_messages(chat_id, [callback_query.message.id, original_command_message.id])
        
        # Enviar el mensaje final
        final_message = await client.send_message(chat_id, end_callbackbtn.format(callback_query.from_user.mention))
        
        # Esperar 5 segundos
        await asyncio.sleep(5)
        
        # Eliminar el mensaje final
        await client.delete_messages(chat_id, final_message.id)