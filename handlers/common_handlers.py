import logging
from pprint import pprint

from telegram import Update, User
from telegram.ext import CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_func(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    pprint(context.user_data)
    pprint(update.message.from_user.first_name)
    pprint(update.effective_user)
    # update.message.reply_text(update.effective_user.username)
    update.message.reply_text('Спасибо, ' + update.message.from_user.first_name + ' ' + update.message.from_user.last_name)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
