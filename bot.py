import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN ="8900156068:AAFtia0IYOQvKzW05UwP96-60N-Yu4akomg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 سلام!\nفایل صوتی بفرست تا دانلودش کنم."
    )

async def get_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ در حال دانلود فایل...")

    audio = update.message.audio or update.message.document

    if not audio:
        await update.message.reply_text("❌ فایل صوتی پیدا نشد")
        return

    os.makedirs("downloads", exist_ok=True)

    file = await context.bot.get_file(audio.file_id)

    path = f"downloads/{audio.file_id}.mp3"

    await file.download_to_drive(path)

    await update.message.reply_text(
        f"✅ فایل دانلود شد!\n\n{path}"
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
    main()    main()
