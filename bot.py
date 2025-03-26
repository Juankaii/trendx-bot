from telegram.ext import Updater, CommandHandler

TOKEN = "7902744811:AAHy2gzDxmL57nBJ9bgF2zbPxg3IDGxcrlk"  # @BotFather theke token diben

def start(update, context):
    update.message.reply_text("🚀 Hello from GitHub Deploy!")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
print("Bot running!")
