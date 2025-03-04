from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from commands.start import start
from commands.roast import roast
from commands.sound import sound
from commands.event import add_event, remove_event, list_events
from commands.registration import add_user, cancel_kyykka, list_users
from utils.users import reset_users


def interpreter(application):
    """ Rekisteröi komennot ja ajastetut tehtävät """
    
    # Komentojen rekisteröinti
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("roast", roast))
    application.add_handler(CommandHandler("sound", sound))
    application.add_handler(CommandHandler("hep", add_user))
    application.add_handler(CommandHandler("list", list_users))
    application.add_handler(CommandHandler("help", start))
    application.add_handler(CommandHandler("cancel", cancel_kyykka))
    application.add_handler(CommandHandler("kalkkaroidaan", add_event))
    application.add_handler(CommandHandler("eipas", remove_event))
    application.add_handler(CommandHandler("seuraava", list_events))
    
    # Ajastetut tehtävät
    job_queue = application.job_queue
    job_queue.run_daily(
        reset_users, 
        time=datetime.time(hour=11, minute=0, second=0), 
        days=(0,)
    )
    
    application.run_polling()

