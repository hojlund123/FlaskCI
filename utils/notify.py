import requests

def send_notification(message, webhook_url):
    payload = {'text': message}
    requests.post(webhook_url, json=payload)
