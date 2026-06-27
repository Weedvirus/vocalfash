import os
import subprocess
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8900156068:AAHet793DtNiQCgP5oFCm3RdF4pdBTN7TlE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 سلام!\nفایل آهنگ را بفرست تا وکال و بیت را جدا کنم."
    )

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ در حال دانلود فایل...")

    audio = update.message.audio or update.message.document

    if not audio:
        await update.message.reply_text("❌ لطفاً یک فایل صوتی ارسال کن.")
        return

    file = await context.bot.get_file(audio.file_id)

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    input_path = f"downloads/{audio.file_id}.mp3"
    await file.download_to_drive(input_path)

    await update.message.reply_text("🎶 در حال جداسازی وکال... این کار چند دقیقه طول می‌کشد.")

    try:
        subprocess.run(
            ["demucs", input_path, "-o", "output"],
            check=True
        )

        song_name = os.path.splitext(os.path.basename(input_path))[0]
        base = f"output/htdemucs/{song_name}"

        vocal_path = f"{base}/vocals.wav"
        instrumental_path = f"{base}/no_vocals.wav"

        if os.path.exists(vocal_path):
            await update.message.reply_audio(audio=open(vocal_path, "rb"), caption="🎤 وکال")

        if os.path.exists(instrumental_path):
            await update.message.reply_audio(audio=open(instrumental_path, "rb"), caption="🎵 بیت")

    except Exception as e:
        await update.message.reply_text(f"❌ خطا:\n{e}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.AUDIO | filters.Document.AUDIO, handle_audio)
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
