from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Função de comando start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou o seu bot.')

# Função de comando help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Envie /start para começar a conversar com o bot.')

# Função principal que inicia o bot
def main():
    # Coloque o token do seu bot aqui
    token = "SEU_TOKEN_AQUI"
    
    # Criação do Updater com o token
    updater = Updater(token)

    # Obtenção do dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Registrar os comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Iniciar o bot
    updater.start_polling()

    # Manter o bot rodando até ser parado
    updater.idle()

if __name__ == '__main__':
    main()
