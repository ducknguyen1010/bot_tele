from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import OPENWEATHER_API_KEY, TELEGRAM_BOT_TOKEN
from handlers.common import help_command, helps_command, start
from handlers.price import price_command
from handlers.ollama import chat_command
from handlers.weather import handle_message, weather_command


def main() -> None:
    if not TELEGRAM_BOT_TOKEN or not OPENWEATHER_API_KEY:
        raise RuntimeError("Thiếu TELEGRAM_BOT_TOKEN hoặc OPENWEATHER_API_KEY")

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("helps", helps_command))
    app.add_handler(CommandHandler("price", price_command))
    app.add_handler(CommandHandler("chat", chat_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == "__main__":
    main()
