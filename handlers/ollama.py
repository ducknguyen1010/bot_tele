from telegram import Update
from telegram.ext import ContextTypes

from services.ollama import get_chat_message


async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    prompt = " ".join(context.args).strip()
    if not prompt:
        await update.message.reply_text("Hay dung: /chat <noi dung>")
        return

    message = get_chat_message(prompt)
    await update.message.reply_text(message)
