from telegram.ext import Updater


def main():
    #Instanciamos el updater
    updater = Updater(token=open('1190910540:AAHI-xZIi_uD02zU62tGv1xe2m2jt5RjBRk').read(), use_context=True)
    
    #añadiendo un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #Pedimos notificaciones a Telegram
    updater.start_polling()

    #capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Hola, soy un bot')

def repite(update, context):
    update.message.reply_text(update.menssage.text)

def suma(update, context):
    resultado = int(context.args [0]) + int(context.args [1])
    resultado = str(resultado)
    update.message.reply_text('El resultado es ' + resultado)

main()
