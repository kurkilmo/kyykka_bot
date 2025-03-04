from telegram.ext import ApplicationBuilder
from config import TG_TOKEN
from interpreter import interpreter

def main():
    """ Pääfunktio, joka alustaa ja käynnistää botin """
    application = ApplicationBuilder().token(TG_TOKEN).build()
    interpreter(application)

if __name__ == "__main__":
    main()

