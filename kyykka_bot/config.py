import os
from dotenv import load_dotenv

# Ladataan .env-tiedosto
load_dotenv('/Users/nikoiljin/tgBot/kyykkäprojekti/.env')

# Telegram Botin Token ja Chat ID
TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Roast-viestit
ROASTS = [
    "{target}, oliko tuo heitto vai yrititkö vain tehdä vaikutuksen nurmikkoon?",
    "{target}, jos tavoitteesi oli osua ohi, onnittelut täydellisestä suorituksesta!",
    "{target}, se heitto oli niin pehmeä, että jopa mummosi olisi nauranut.",
    "{target}, onko tuo kyykkämaila vai harava? Koska näytät vaan möyhivän maata.",
    "{target}, luulin katsovani kyykkää, en curlingia – työnnä vaan vähän lisää!",
    "{target}, oliko tuo strategia vai vahinko? Koska se näytti lähinnä avunhuudolta.",
    "{target}, kun sanottiin 'tähtää', tarkoitus oli kohti kyykkiä, ei taivasta.",
    "{target}, luulin, että kyykässä pyritään osumaan, ei piilottamaan kyykkiä heinikkoon.",
    "{target}, hei, kenttä on täällä! Tai siis, jos satut joskus osumaan siihen.",
    "{target}, heititkö kyykkää vai yrititkö ruokkia kaloja? Koska tuo lensi kuin hauen syöttinä!"
]


