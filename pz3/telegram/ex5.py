from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ConversationHandler, ContextTypes, Application)
TOKEN = ''
async def start(update: Update, context):
    await update.message.reply_text('Hello, what you want?')

async def menu(update: Update, context):
    await update.message.reply_text('my menu:\n''/menu - show menu\n''/whisper <text> - say quietly\n''/scream <text> – say loudly')

async def whisper(update: Update, context):
    if context.args:
        text = " ".join(context.args)
        await update.message.reply_text(text.lower())
    else:
        await update.message.reply_text('use /whisper with some text')

async def scream(update: Update, context):
    if context.args:
        text = " ".join(context.args)
        await update.message.reply_text(text.upper()+'!!!')
    else:
        await update.message.reply_text('use /scream with some text')

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('menu', menu))
    app.add_handler(CommandHandler('whisper', whisper))
    app.add_handler(CommandHandler('scream', scream))
    print('bot working')
    app.run_polling()
if __name__ == '__main__':
    main()