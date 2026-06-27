from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8900156068:AAEO_dXnY1RvXyxWyru7K1OfO1PUNvpP_kI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 سلام! یک فایل صوتی بفرست."
    )

async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ فایل با موفقیت دریافت شد!"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.AUDIO | filters.Document.AUDIO,
            get_audio
        )
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
