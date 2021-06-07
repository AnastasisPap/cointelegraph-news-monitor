import requests
from datetime import datetime


def send_webhook(_url, description, embed_title, author):
    webhook_url = 'webhook url'
    current_time = datetime.now().strftime("%H:%M:%S")
    data = {"username": "Bob the builder", "embeds": [
        {
            "title": embed_title,
            "description": f'[{description}]({_url})',
            "color": 1127128,
            "footer": {"text": f"cryptoMalakes [{current_time}]", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/220px-Ethereum-icon-purple.svg.png"},
            "fields": [{"name": "Author", "value": author, "inline": True}],
        }
    ]}

    res = requests.post(webhook_url, json=data)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        print(f"Payload delivered successfully, code{res.status_code}")
