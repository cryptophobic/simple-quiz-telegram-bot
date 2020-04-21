from telegram.ext import Updater

from controllers.controller_quiz import set_handlers
from handlers.common_handlers import error


def main():
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher
    set_handlers(dp)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
