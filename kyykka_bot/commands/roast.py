import random
import re
from telegram import Update
from telegram.ext import ContextTypes
from config import ROASTS

async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Lähettää satunnaisen roastin """
    print(f"Roast from {update.effective_chat.id}")
    text = update.message.text
    target = re.search(r'@[\w_]+', text)
    target_name = target.group(0) if target else "Tähtipelaaja"
    roast_message = random.choice(ROASTS).format(target=target_name)
    await update.message.reply_text(roast_message)

