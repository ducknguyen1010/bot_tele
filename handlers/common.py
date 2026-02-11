from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Dùng lệnh: /weather <địa điểm>. Ví dụ: /weather Ha Noi (địa điểm viết cách, không dấu)\n"
            "Dùng lệnh: /price <ma> để xem giá coin. Ví dụ: /price BTC\n"
            "Dùng lệnh: /chat <noi dung> để hoi Ollama"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Cú pháp: /weather <địa điểm>. Ví dụ: /weather Da Nang (địa điểm viết cách, không dấu)\n"
            "Cú pháp: /price <ma>. Ví dụ: /price ETH\n"
            "Cú pháp: /chat <noi dung>"
        )


async def helps_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await help_command(update, context)
