import datetime

events = { "aika": None, "päivä": None, "job_id": None }

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
    events["job_id"] = None

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


def get_event_datetime():
    """ Palauttaa tapahtuman päivämäärän ja ajan datetime-objektina """
    if not events["aika"] or not events["päivä"]:
        return None
    try:
        return datetime.datetime.strptime(events["päivä"] + " " + events["aika"], "%d.%m.%Y %H:%M")
    except ValueError:
        return None


def set_job_id(job_id):
    """ Tallentaa tapahtumaan liittyvän job ID:n """
    events["job_id"] = job_id


def get_job_id():
    """ Palauttaa tapahtumaan liittyvän job ID:n """
    return events["job_id"]

