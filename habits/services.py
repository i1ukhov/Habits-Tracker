import requests

from config.settings import TG_BOT_API, TG_URL


def send_telegram_message(tg_chat_id, message):
    """Отправляет сообщение в Телеграм через бота"""
    parameters = {"chat_id": tg_chat_id, "text": message}
    r = requests.get(f"{TG_URL}{TG_BOT_API}/sendMessage", params=parameters)
    if r.status_code == 200:
        print("Сообщение отправлено")
    else:
        print("Ошибка отправки")
