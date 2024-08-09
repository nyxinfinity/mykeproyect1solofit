from pyrogram import Client, filters
import time  # Para el mensaje ping
import aiohttp

# Decorador para comandos
def botcmd(cmds: list):
    def decorator(func):
        @Client.on_message(filters.command(cmds, prefixes=["/", "$", ".", "!", "?", "&", "@"]))
        async def wrapper(client, message):
            await func(client, message)
        return wrapper
    return decorator

# Decorador para callback data
def botbutton(data: str = None):
    def decorator(func):
        async def wrapper(client, callback_query):
            try:
                # Llama a la función decorada
                await func(client, callback_query)
            except Exception as e:
                print(f"Error en el callback: {e}")
        # Registra el manejador de callback_query en el cliente
        Client.on_callback_query(filters.regex(data))(wrapper)
        return wrapper
    return decorator
