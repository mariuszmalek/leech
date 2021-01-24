import os
import json
from . import show_in_console

config = None

def configFile():
    if dosyaMevcutMu("config.json"):
        with open('config.json', 'r+', encoding="utf-8") as dosya:
            config = json.load(dosya)
    else:
        show_in_console("Config file is missing - Config dosyası eksik !",2)
        exit()

def get_config(anahtar):
    deger = config
    for key in anahtar.split('.'):
        deger = deger[key]
    return deger

def dosyaMevcutMu(path):
    if os.path.isfile(path):
        return True
    else:
        return False