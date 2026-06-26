from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = ""8900156068:AAH2NwFsfwAzf8RHUJHng9NPdBO3kSuSkD0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 🎵\n"
        "فعلاً نسخه آزمایشی بات فعال است.\n"
        "برای جدا کردن وکال، فایل آهنگ را بفرست."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
