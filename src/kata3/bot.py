import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text('Hola, Geeks!')

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text('Ayudame!')

def mayus(update, context):
        # Mensaje a partir del areglo de argumentos.
        msj = ""
        for m in context.args:
            msj += m + ' '
        
        # Pasamos el mensaje a mayusculas
        msj_mayusculas = msj.upper()
        return msj_mayusculas

def alreves(update, context):
    """Repite el mensaje del usuario."""
    msj_alreves = ""
        for m in context.args:
            msj_alreves += m[::-1] + ' '
            
    return msj_alreves

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    # Añadiendo un manejador al comando /start
    dp.add_handler(CommandHandler("start", start))
    
    # Añadiendo un manejador al comando /help
    dp.add_handler(CommandHandler("help", help))

    # Añadiendo un manejador al comando /mayus
    dp.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    dp.add_handler(MessageHandler(Filters.text, alreves))
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
