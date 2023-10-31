from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    filters,
    MessageHandler,
)
from celery_tasks import send_message_task


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    message_sender = update.effective_user.first_name

    send_message_task.delay(message_text, message_sender)

    await update.message.reply_text("Message sent to server")


app = (
    ApplicationBuilder().token("6837382073:AAFWxN02Nx6FHnTWr6Tl8owbuW-TudZR3Sc").build()
)
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
