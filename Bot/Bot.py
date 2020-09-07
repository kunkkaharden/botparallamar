
import json
import Servicios
import datetime
import os
import requests
from flask import Flask, request
from datetime import datetime,time
from 

BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable

app = Flask(__name__)

servicio = Servicios.Servicios()

@app.route('/',methods=['Post'])
def main():
    sms = request.json
    info = info_mensaje(sms)
    print(sms)
    if not info.id_persona == None:
        if not info.is_bot:
            servicio.analizarPersona(info.id_persona, info.persona)
    if not info.is_bot and info.tipo_sms == "texto":
        enviar_mensaje();


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)