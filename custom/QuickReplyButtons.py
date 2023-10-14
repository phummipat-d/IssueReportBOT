#ไฟล์นี้จะใช้ข้อมูลการแสดงผลจากไฟล์ QuickButtonsItems.py
#สามารถปรับแก้ฟังก์ชัน ReplyQuickButtons เพื่อส่งค่าไปยังฟังก์ชัน getButtonsItems ในไฟล์ QuickButtonsItems.py ได้

from linebot.models import *
from linebot.exceptions import *
from custom.Config import *
import json
import requests
from custom.QuickButtonsItems import getButtonsItems,getButtonsUnitItems

def ReplyQuickButtons(line_bot_api,replyToken,title,iType=1):
    items = getButtonsItems()
    if iType == 2:
        items = getButtonsUnitItems()
        
    text_message = TextSendMessage(text=title,
        quick_reply=QuickReply(
            items=items
        )
    )

    line_bot_api.reply_message(replyToken,text_message)
    return 200