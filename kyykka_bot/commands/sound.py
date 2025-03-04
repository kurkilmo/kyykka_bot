from telegram import Update
from telegram.ext import ContextTypes

async def sound(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Toistaa äänen """
    await update.message.reply_audio(audio="https://www.myinstants.com/media/sounds/roblox-death-sound_1.mp3")

