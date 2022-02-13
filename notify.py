import config
from flask import Flask
from flask import request, render_template, flash
from linebot import LineBotApi
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)
line_bot_api = LineBotApi(config.key['linebotAPI'])

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello,Notify service!"

@app.route('/push')
def push_message():
     #push message to one user
    line_bot_api.push_message('U0d72b82f859f120e40ecbef2919c7384', TextSendMessage(text='哈囉!我是Push Message！'))
    return str("ok")
@app.route('/push_broadcast')
def push_message_broadcast():  
    carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://health99.hpa.gov.tw/storage/images/articles/3947145_m.jpg',text='對抗COVID-19 力行「護心行動」', 
            actions=[
                URIAction(label='查看內容', uri='https://health99.hpa.gov.tw/news/18131')
            ]),
            CarouselColumn(thumbnail_image_url='https://health99.hpa.gov.tw/storage/images/articles/3947145_m.jpg',text='及早控制高血壓 降低主動脈剝離',  
            actions=[
                URIAction(label='查看內容', uri='https://health99.hpa.gov.tw/news/18127')
            ]),
        ]) 
    template_message = TemplateSendMessage(alt_text='衛教文章', template=carousel_template)   
    line_bot_api.broadcast(template_message)
    return str("ok")
   
    # line_bot_api.multicast()
  
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5001, debug=True)
    app.run()
