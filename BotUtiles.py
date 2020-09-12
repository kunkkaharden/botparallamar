import requests
class Info_Mensaje():
    def __init__(self ,persona, id_persona, bot, chat, id_chat, tipo_chat, tipo_sms,date,update_id):
        self.persona = persona
        self.id_persona = id_persona
        self.is_bot = bot
        self.chat = chat
        self.id_chat = id_chat
        self.tipo_chat = tipo_chat
        self.tipo_sms = tipo_sms
        self.date = date
        self.update_id = update_id


def info_mensaje(mensaje):
    tipo_sms = "texto_editado"
    tipo_chat = None
    chat = None
    update_id = None
    persona = None
    id_persona = None
    bot = None
    id_chat = None
    date = None
    if "message" in mensaje:
        if "text" in mensaje["message"]:
            tipo_sms = "texto"
        elif "sticker" in mensaje["message"]:
            tipo_sms = "sticker"
        elif "animation" in mensaje["message"]:
            tipo_sms = "animacion"
        elif "photo" in mensaje["message"]:
            tipo_sms = "foto"
        else:
            tipo_sms = "otro"

        tipo_chat = mensaje['message']['chat']['type']

        chat = ""
        if not tipo_chat.lower() == "private":
            chat = mensaje['message']['chat']['title']
        else:
            chat = tipo_chat

        update_id = mensaje['update_id']
        persona = mensaje['message']['from']['first_name']
        id_persona = mensaje['message']['from']['id']
        bot = mensaje['message']['from']['is_bot']
        id_chat = mensaje['message']['chat']['id']
        date = mensaje['message']['date']
    return Info_Mensaje(persona, id_persona, bot, chat, id_chat, tipo_chat, tipo_sms, date, update_id)

def leer_mensaje(mensaje):
    texto = mensaje['message']['text']
    return texto

def enviar_mensaje(BOT_URL ,idChat, texto):
    json_data = {
        "chat_id": idChat,
        "text": texto,
    }
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=json_data)
    return ''


def mencion(id_user):
    return ''

def obtenernick(mensaje):
    nick = ""
    if "message" in mensaje:
        if "username" in mensaje["message"]:
            nick = mensaje["message"]["from"]["username"]

    return nick