from linebot.models import *
from linebot.exceptions import *

def ReplyTextMessage(line_bot_api,replyToken, txtMessage ):
    textMessage = TextSendMessage(text=txtMessage)
    line_bot_api.reply_message(replyToken,textMessage)
    return 200

def ReplyImageMessage(line_bot_api,replyToken, originalContentUrl,previewImageUrl):
    image_message = ImageSendMessage(
        original_content_url=originalContentUrl,
        preview_image_url=previewImageUrl
    )
    line_bot_api.reply_message(replyToken,image_message)
    return 200

def ReplyVideoMessage(line_bot_api,replyToken, originalContentUrl,previewImageUrl):
    video_message = VideoSendMessage(
        original_content_url=originalContentUrl,
        preview_image_url=previewImageUrl
    )
    line_bot_api.reply_message(replyToken,video_message)
    return 200

def ReplyAudioMessage(line_bot_api,replyToken, originalContentUrl):
    audio_message = AudioSendMessage(
        original_content_url=originalContentUrl,
        duration=240000
    )
    line_bot_api.reply_message(replyToken,audio_message)
    return 200

def ReplyLocationMessage(line_bot_api,replyToken, title,address,latitude,longitude):
    location_message = LocationSendMessage(
        title=title,
        address=address,
        latitude=latitude,
        longitude=longitude
    )
    line_bot_api.reply_message(replyToken,location_message)
    return 200

def ReplyStickerMessage(line_bot_api,replyToken, package_id,sticker_id):
    sticker_message = StickerSendMessage(
        package_id=package_id,
        sticker_id=sticker_id
    )
    line_bot_api.reply_message(replyToken,sticker_message)
    return 200
        