import datetime

events = { "aika": None, "päivä": None }

def onko_tuleva_tapahtuma():
    """ Tarkistaa onko tapahtuma tulevaisuudessa """
    if not events["aika"] or not events["päivä"]:
        return False
    event_time = datetime.datetime.strptime(events["päivä"] + " " + events["aika"], "%d.%m.%Y %H:%M")
    current_time = datetime.datetime.now()
    return event_time > current_time

def reset_event():
    """ Nollaa tapahtuman """
    events["aika"] = None
    events["päivä"] = None

def add_new_event(aika: str, päivä: str):
    """ Lisää uuden tapahtuman """
    events["aika"] = aika
    events["päivä"] = päivä
    print(events)

def remove_current_event():
    """ Poistaa nykyisen tapahtuman """
    reset_event()

def get_next_event():
    """ Palauttaa seuraavan tapahtuman """
    if onko_tuleva_tapahtuma():
        return f"{events['päivä']} klo {events['aika']}"
    return None

