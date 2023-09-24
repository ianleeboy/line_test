from flask import Flask, request, abort
from line_bot_api import *
from config import Config

from extensions import db, migrate
from models.user import User
from events.admin import *
from events.service import *

from urllib.parse import parse_qsl
import os

app = Flask(__name__)

app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevConfig'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_t7rg_user:9PB6Yz2ZdSAGbSVu3fOJkFaQbwfEWxVo@dpg-ck7tbh7sasqs73cc6smg-a.singapore-postgres.render.com/test_t7rg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
migrate.init_app(app, db)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message_text = str(event.message.text).lower()
    user = User.query.filter(User.line_id == event.source.user_id).first()

    if not user:
        profile = line_bot_api.get_profile(event.source.user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)

        user = User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(user)
        db.session.commit()


    print(user.id)
    print(user.line_id)
    print(user.display_name)

    if message_text == '@預約服務':
        service_category_event(event)

    elif message_text == '我想重新預約':
        service_category_event(event)

    elif message_text.startswith('*'):
        if event.source.user_id not in ['U636a012c9911a5eda79688a80bb2f7fd']:
            return
        if message_text in ['*data', '*d']:
            list_reservation_event(event)


@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))

    if data.get('action') == 'service':
        service_event(event)
    elif data.get('action') == 'select_date':
        service_select_date_event(event)
    elif data.get('action') == 'select_time':
        service_select_time_event(event)
    elif data.get('action') == 'confirm':
        service_confirm_event(event)
    elif data.get('action') == 'confirmed':
        service_confirmed_event(event)
    elif data.get('action') == 'cancel':
        service_cancel_event(event)


if __name__ == "__main__":
    app.run()