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

line_bot_api = LineBotApi('DZ4OhXtBO550KrjBM4JemqMZjynGUATvdYFWXPSznxg2Loe7H3/sdHD2Kx+nGDtnwFxzGrtXrkOqTk4TwaJp89xF2AV2kpoIxZUbG+t76gl+LK/7WwtRmMR8gF+NpI0nv0yxwWP1dkBpiyzz6naDSgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0337f75765a28d2aa6ac7268ef6d8d37')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.test
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()