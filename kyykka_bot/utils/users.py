from config import CHAT_ID
from utils.events import get_next_event

registered_users = []

def register_user(username):
    if (get_next_event() == None):
        return "Kyykkä-tapahtumaa ei ole vielä lisätty. Käytä /kalkkaroidaan komentoa lisätäksesi tapahtuman."
    if username not in registered_users:
        registered_users.append(username)
        return f"{username} on rekisteröitynyt kyykkä-tapahtumaan!"
    return f"{username}, olet jo rekisteröitynyt kyykkä-tapahtumaan."

def unregister_user(username):
    if username in registered_users:
        registered_users.remove(username)
        return f"{username} on poistettu kyykkä-tapahtumasta."
    return f"{username}, et ole rekisteröitynyt kyykkä-tapahtumaan."

def list_registered_users():
    return registered_users

async def reset_users(context):
    global registered_users
    registered_users = []
    await context.bot.send_message(
        chat_id=CHAT_ID, 
        text="Tämän viikon ilmoittautuminen on alkanut. Ilmoittaudu mukaan käyttämällä /hep komentoa.\n"
             "Muista myös tarkistaa osallistujalista /list komennolla.\n"
             "Pidetään hauskaa ja nähdään kyykkäkentällä! 🎉"
    )

