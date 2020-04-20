import logging
import re
from pprint import pprint

from telegram import Update, User
from telegram.ext import CallbackContext

# Enable logging
from models.quiz import Quiz

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
quiz = Quiz()


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_func(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""

    # update.message.reply_text(update.effective_user.username)
    # update.message.reply_text('Спасибо, ' + update.message.from_user.first_name + ' ' + update.message.from_user.last_name)
    print(update.message.text)
    result = 'Неправильно!'
    if update.message.text.lower() == 'хз':
        quiz.next_question()
        result = 'Пропускаем!'

    if quiz.match_answer(update.message.text):
        result = "Правильно!"

    if quiz.match_answer(update.message.text) or quiz.attempts_number() > 4:
        quiz.next_question()

    update.message.reply_text(
        "{}\n{}\n\n{} {} букв".format(
            result,
            quiz.get_current_question(),
            quiz.display_answer(),
            len(quiz.display_answer())
        ))


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
