from telegram import Update
from telegram.ext import ContextTypes

from services.coin import get_price_message


async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    symbol = " ".join(context.args).strip().upper()
    if not symbol:
        await update.message.reply_text("Hãy dùng: /price <mã coin>")
        return

    message = get_price_message(symbol)
    await update.message.reply_text(message)
