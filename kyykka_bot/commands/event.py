import re
from telegram import Update, ChatMember
from telegram.ext import ContextTypes
from utils.events import add_new_event, remove_current_event, get_next_event, get_event_datetime, set_job_id, get_job_id
from utils.users import reset_users


async def is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    # Hakee käyttäjän chat-tiedot
    member = await context.bot.get_chat_member(chat_id, user_id)
    
    # Tarkistaa, onko käyttäjä ylläpitäjä tai omistaja
    return member.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]


async def add_event(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await is_admin(update, context):
        await update.message.reply_text("Tämä komento on vain ylläpitäjille. 🚫")
        return
    """ Lisää uuden kyykkä-tapahtuman """
    text = update.message.text
    event_time = re.search(r'\d{2}:\d{2}', text)
    event_day = re.search(r'\d{2}\.\d{2}\.\d{4}', text)

    if event_time and event_day:
        aika = event_time.group(0)
        päivä = event_day.group(0)
        add_new_event(aika, päivä)
        
        # Hae tapahtuman aika ja ajoita resetti
        event_datetime = get_event_datetime()
        if event_datetime:
            job = context.job_queue.schedule_once(
                reset_users,
                when=event_datetime,
                name=f"event_reset_{päivä}_{aika}"
            )
            set_job_id(job.id)
        
        await update.message.reply_text(f"Kyykkä-tapahtuma lisätty: {päivä} klo {aika}")
    else:
        await update.message.reply_text("Anna päivämäärä ja aika muodossa: dd.mm.yyyy hh:mm")

async def remove_event(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await is_admin(update, context):
        await update.message.reply_text("Tämä komento on vain ylläpitäjille. 🚫")
        return
    """ Poistaa nykyisen tapahtuman """
    # Peruuta aiemmin ajoitettu resetti-job
    job_id = get_job_id()
    if job_id:
        context.job_queue.get_jobs_by_name(job_id)
        for job in context.job_queue.jobs():
            if job.id == job_id:
                job.schedule_removal()
    
    remove_current_event()
    await reset_users(context)
    await update.message.reply_text("Kyykkä-tapahtuma poistettu.")

async def list_events(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Listaa tulevat tapahtumat """
    event = get_next_event()
    if event:
        await update.message.reply_text(f"Seuraava kyykkä-tapahtuma: {event}")
    else:
        await update.message.reply_text("Ei tulevia kyykkä-tapahtumia.")

