from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8900156068:AAHoGMlyeiwhk5FLdcLZoOBZOTR6W8Ppt_0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 🎵\nبات با موفقیت روشن شد!"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
