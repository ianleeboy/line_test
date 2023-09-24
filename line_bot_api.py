from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,
    FlexSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackAction, PostbackEvent,
    QuickReplyButton, QuickReply, ConfirmTemplate, MessageAction, ButtonsTemplate
)
from linebot.models import *


line_bot_api = LineBotApi('AOH/hj5Q7s99bvqyBA5Zo1XTH5CZPIiEU2RzGQYRAFqX4BSETr7SdllGl4GZBIF2MGUVHBaCbfd25nbBgTEjgQlu2d/tIHWCzaehRNvKSvPaiVg6ROHtgBf3c3mt3tm6DYMKMBiB9nn0OS3sSxnQxAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('69f9dd5da2d25c8008b0b4019b20b159')