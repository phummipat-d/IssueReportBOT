
#ไฟล์นี้จะใช้ข้อมูลสไตล์การแสดงผลจากไฟล์ FlexMessage.py
#สามารถปรับแก้ฟังก์ชัน ReplyFlexMessage เพื่อส่งค่าไปยังฟังก์ชัน getFlexMessage ในไฟล์ FlexMessage.py ได้
from linebot.models import *
from custom.FlexMessage import getFlexMessage
import json

def ReplyFlexMessage(line_bot_api,replyToken,alt_text):
    flex = getFlexMessage("Good")
    flex = json.loads(flex)
    flexMessage = FlexSendMessage(alt_text=alt_text,contents=flex)
    line_bot_api.reply_message(replyToken,flexMessage)
    return 200