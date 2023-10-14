#ไฟล์นี้จะเป็นการตั้งค่ารูปแบบการแสดงผลที่จะส่งไปให้กับผู้ใช้งาน และไฟล์นี้เป็นส่วนดึงข้อมูลจาก API มาแสดงผลในรูปแบบที่กำหนด
#การออกแบบการแสดงผลสามารถศึกษาได้จากรายละเอียดตาม https://developers.line.biz/flex-simulator/ 
#และเมื่อทำการออกแบบเรียบร้อยให้ copy ไฟล์ json มาแทนที่ใน ตัวแปร flexmessage
import json
def getFlexMessage(txtLael):
    flexmessage =  {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            },
            {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#999999",
                "margin": "md",
                "flex": 0
            }
            ]
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
            {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "Place",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 5
                }
                ]
            },
            {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "Time",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": "10:00 - 23:00",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 5
                }
                ]
            }
            ]
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "CALL",
            "uri": "https://linecorp.com"
            }
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "WEBSITE",
            "uri": "https://linecorp.com"
            }
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "Add",
            "uri": "https://linecorp.com"
            }
        }
        ],
        "flex": 0
    }
    }

    return json.dumps(flexmessage)