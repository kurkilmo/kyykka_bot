from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Tervetuloviesti ja komennot """
    await update.message.reply_text(
        "Tervetuloa Kyykkäbotin maailmaan! 🎉\n"
        "Tässä ovat käytettävissä olevat komennot:\n\n"
        "/roast - Saat satunnaisen roastin, joka varmasti piristää päivääsi!\n"
        "/hep - Ilmoittaudu kyykkä-tapahtumaan ja varmista paikkasi pelissä.\n"
        "/list - Listaa kaikki kyykkä-tapahtumaan ilmoittautuneet käyttäjät.\n"
        "/kalkkaroidaan - Lisää uusi kyykkä-tapahtuma kalenteriin. Käyttöohje: /kalkkaroidaan dd.mm.yyyy hh:mm\n"
        "/eipas - Poista olemassa oleva kyykkä-tapahtuma.\n"
        "/seuraava - Näytä seuraava kyykkä-tapahtuma ja sen tiedot.\n"
        "/cancel - Peru ilmoittautumisesi kyykkä-tapahtumasta.\n"
        "/help - Näytä tämä viesti uudelleen, jos tarvitset apua."
    )

