from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('EnYM+Vu3YMk8L7xkfYxB5NhEVYd4YGDvsgCU953WzxKQmj3hYtBGAa2egKR9tryX9yn/+KkA1KAtd7ftuyBbSR68qDkm9Kn9HNe16Y6zz/fF7DX5xRl47vMc/WdodDbJK9VpKwFJaGUYT6QPP3dbfgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b207380d0772dfd246e1f05c93f376dc')


@app.route("/callback", methods=['POST'])
def callback():
    print(request.get_data(as_text=True));

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    print(message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )


if __name__ == "__main__":
    app.run()
