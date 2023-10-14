
def getButtonsItems():
    data = [
        ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png","ตรวจสอบข้อมูล","ตรวจสอบข้อมูล"],
        ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png","บันทึกข้อมูล","บันทึกข้อมูล"]
    ]

    items = []
    for item in data:
        button = {
            "type": "action", 
            "imageUrl":item[0],
            "action": {
                "type": "message",
                "label": item[1],
                "text": item[2]
            }
        }
        items.append(button)
    
    return items


def getButtonsUnitItems():
    data = []
    from db.unit import Unit
    u = Unit()
    units_name = u.Select()
    
    for name in units_name:
        a = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",name[1],name[1]]
        data.append(a)

    items = []
    for item in data:
        button = {
            "type": "action", 
            "imageUrl":item[0],
            "action": {
                "type": "message",
                "label": item[1],
                "text": item[2]
            }
        }
        items.append(button)
    
    return items