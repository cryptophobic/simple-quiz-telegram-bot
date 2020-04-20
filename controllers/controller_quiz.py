from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

from handlers.common_handlers import echo, help_func, start


def set_handlers(dispatcher: Dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_func))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))
