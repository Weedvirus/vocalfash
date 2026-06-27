import os
import subprocess
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8900156068:AAHet793DtNiQCgP5oFCm3RdF4pdBTN7TlE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 سلام!\nفایل MP3 یا آهنگ را بفرست تا وکال و بیت را جدا کنم."
    )


async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ فایل دریافت شد")
    await update.message.reply_text("⏳ در حال دانلود فایل...")

    audio = update.message.audio or update.message.document

    if not audio:
        await update.message.reply_text("❌ لطفاً فایل صوتی ارسال کن.")
        return

    os.makedirs("downloads", exist_ok=True)

    file = await context.bot.get_file(audio.file_id)
    input_path = f"downloads/{audio.file_id}.mp3"

    await file.download_to_drive(input_path)

    await update.message.reply_text(
        "🎶 فایل دانلود شد.\nفعلاً تست دریافت فایل موفق بود."
    )

    # بعداً کد Demucs را اضافه می‌کنیم


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.AUDIO | filters.Document.AUDIO,
            handle_audio
        )
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
