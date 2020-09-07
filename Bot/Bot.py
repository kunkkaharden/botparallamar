
import json
#import Servicios
import datetime
import os
import requests
from flask import Flask, request
from datetime import datetime,time
from Utiles.BotUtiles import *

BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable

app = Flask(__name__)


@app.route('/',methods=['Post'])
def main():
    sms = request.json
    info = info_mensaje(sms)

    if not info.is_bot and info.tipo_sms == "texto":
        enviar_mensaje();


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)