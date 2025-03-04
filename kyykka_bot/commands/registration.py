from telegram import Update
from telegram.ext import ContextTypes
from utils.users import register_user, unregister_user, list_registered_users

async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Lisää käyttäjän tapahtumaan """
    user = update.message.from_user
    response = register_user(user.username)
    await update.message.reply_text(response)

async def cancel_kyykka(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Poistaa käyttäjän ilmoittautumisen """
    user = update.message.from_user
    response = unregister_user(user.username)
    await update.message.reply_text(response)

async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Listaa kaikki rekisteröityneet käyttäjät """
    users = list_registered_users()
    if users:
        await update.message.reply_text("Ilmottautuneet kalggarit:\n" + "\n".join(users))
    else:
        await update.message.reply_text("Ei rekisteröityneitä käyttäjiä.")

