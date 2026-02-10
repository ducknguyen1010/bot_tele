from telegram import Update
from telegram.ext import ContextTypes

from services.weather import get_weather_message
from utils.text import extract_location


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    location = " ".join(context.args).strip()
    if not location:
        await update.message.reply_text("Hãy dùng: /weather <địa điểm>")
        return

    message = get_weather_message(location)
    await update.message.reply_text(message)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    text = update.message.text or ""
    location = extract_location(text)
    if location:
        message = get_weather_message(location)
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Hãy dùng: /weather <địa điểm>")
