
#ไฟล์นี้จะเป็นไฟล์เริ่มต้นสำหรับการพัฒนาระบบ
#ตัวแปร payload คือข้อมูลที่ถูกส่งมาจากฝั่งผู้ใช้งาน(LineApp)
#การตอบกลับข้อมูลไปให้ผู้ใช้งานฝั้ง LineApp แบบพื้นฐานเช่น ข้อมูล,ภาพ ฯลฯ จะใช้การ Reply ผ่าน basic packages (BasicReplyMessage)
#การตอบกลับข้อมูลไปให้ผู้ใช้งานฝั้ง LineApp ในรูปแบบที่ซับซ้อนมากขึ้น เช่น FlexMessage จะใช้การ Reply ผ่าน custom packages

from custom.Config import *
from basic.BasicReplyMessage import *
from custom.ReplyFlexMessage import ReplyFlexMessage
from custom.QuickReplyButtons import ReplyQuickButtons
from custom.PublicURL import public_root_url

class Buffer:
    items = {"userId":"Initialization"}
    images = {"userId":"Initialization"}
    pushMessageCount = 0

def manage(line_bot_api,payload):
    message_type = "None"
    replyToken = "None"
    try:
        message_type = payload['events'][0]['message']['type']
        replyToken = payload['events'][0]['replyToken']
    except Exception as e:
        return 200

    #isRedelivery = payload['events'][0]['deliveryContext']['isRedelivery']
    #print(payload)
    #print("===============")
    
    #กรณีผู้ใช้งานส่งข้อความเป็น text
    if message_type == "text" :
        try:
            #รับข้อความที่ได้จากผู้ใช้งาน
            txtMessage = payload['events'][0]['message']['text']
            if txtMessage == "ร้องเรียน":
                userId = payload['events'][0]['source']['userId']
                profile = line_bot_api.get_profile(userId)
                displayName = profile.display_name
                Buffer.items.update({userId: [userId,displayName,"-","-","รอตรวจสอบ",0.0,0.0,"-"]})
                Buffer.images.update({userId: []})
                sendMessageManager(line_bot_api,replyToken,userId,"ระบุชื่อ-สกุลผู้ร้องเรียน")

            elif txtMessage == "ตรวจสอบข้อมูล":
                userId = payload['events'][0]['source']['userId']
                if userId in Buffer.items :
                    items = Buffer.items[userId]
                    txtAppeal = "ข้อมูลการร้องเรียนของท่าน\n"
                    txtAppeal = txtAppeal+"ชื่อ Line: " + items[1] + "\n"
                    txtAppeal = txtAppeal+"ชื่อ-สกุลผู้ร้องเรียน: " + items[2] + "\n"
                    txtAppeal = txtAppeal+"รายละเอียดการร้องเรียน: " + items[3] + "\n"
                    txtAppeal = txtAppeal+"พิกัด: " + str(items[5]) +"," + str(items[6])+ "\n"
                    txtAppeal = txtAppeal+"หน่วยงาน: " + str(items[7]) + "\n"
                    images = Buffer.images[userId]
                    txtAppeal = txtAppeal+"จำนวนภาพที่แนบ : " +str(len(images)) + "\n"
                    #print("num of images",len(images))

                    root_url = public_root_url()
                    public_url = root_url.get_public_url()

                    for i in range(len(images)):
                        image_info = images[i]
                        image_url = public_url + "/" + image_info[0] + ".png"
                        txtAppeal = txtAppeal +str((i+1))+". "+ image_url + "\n"

                    txtAppeal = txtAppeal+"\n- ท่านสามารถแนบไฟล์ภาพเพื่่อเป็นหลักฐานเพิ่มได้\n"
                    txtAppeal = txtAppeal+"- กรุณาตรวจสอบข้อมูลก่อนบันทึก\n"
                    txtAppeal = txtAppeal+"- หากต้องการแก้ข้อมูลให้ทำการเลือกเมนู 'ร้องเรียน' อีกครั้ง\n"
                    sendQuickReplyManager(line_bot_api,replyToken,userId,txtAppeal)
                else:
                    sendMessageManager(line_bot_api,replyToken,userId,"ท่านยังไม่ได้กรอกข้อมูลร้องเรียน")

            elif txtMessage == "บันทึกข้อมูล":
                userId = payload['events'][0]['source']['userId']
                if userId in Buffer.items :
                    items = Buffer.items[userId]
                    #print(items)
                    from db.appeal import AppealInfo
                    appeal = AppealInfo()
                    id = 0
                    if items[3] != "-" and items[7] != "": 
                        id = appeal.Insert(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7])

                    if id > 0 :
                        dbResponse = "บันทึกข้อมูลเรียบร้อย" 
                        if userId in Buffer.images:
                            images = Buffer.images[userId]
                            for image in images:
                                appeal.InsertImage(image[0],image[1],id)
                            
                            if userId in Buffer.images:
                                del Buffer.images[userId]
                            
                            dbResponse = dbResponse + "\nบันทึกภาพเรียบร้อย" 
                        
                        del Buffer.items[userId]
                        sendMessageManager(line_bot_api,replyToken,userId,dbResponse)
                    else:
                        sendMessageManager(line_bot_api,replyToken,userId,"บันทึกข้อมูลไม่สำเร็จ \nกรุณาตรวจสอบข้อมูลแล้วลองอีกครั้ง")
                else:
                    sendMessageManager(line_bot_api,replyToken,userId,"ท่านยังไม่ได้กรอกข้อมูลร้องเรียน")

            elif txtMessage == "สถานะภาพการร้องเรียนก่อนหน้า":
                userId = payload['events'][0]['source']['userId']
                from db.appeal import AppealInfo
                #print(userId)
                result = AppealInfo.Select("userId = '"+str(userId)+"'")
                content = ""
                for row in result:
                    content = content + "ร้องเรียน : " + str(row[4]) + "\n"
                    content = content + "สถานะ : " + str(row[5]) + " ["+str(row[9])+"]\n"
                    content = content + "====================\n\n" 
                sendMessageManager(line_bot_api,replyToken,userId,content)

            else:
                userId = payload['events'][0]['source']['userId']
                items = Buffer.items[userId]

                if items[0] == userId:
                    if items[2] == "-":
                        items[2] = txtMessage
                        sendMessageManager(line_bot_api,replyToken,userId,"ระบุรายละเอียดการร้องเรียน")

                    elif items[3] == "-":
                        items[3] = txtMessage
                        #sendMessageManager(line_bot_api,replyToken,userId,"ระบุหน่วยงาน")
                        sendQuickReplyManager(line_bot_api,replyToken,userId,"ระบุหน่วยงานที่ต้องการแจ้ง",2)
                        
                    elif items[7] == "-":
                        items[7] = txtMessage
                        sendMessageManager(line_bot_api,replyToken,userId,"ระบุพิกัด")

        except Exception as e:
            return 200
            
    elif message_type == "location":
        try:
            userId = payload['events'][0]['source']['userId']
            items = Buffer.items[userId]
            if userId in Buffer.items :
                if items[0] == userId:
                    if items[5] == 0.0 or items[6] == 0.0:
                        items[5] = payload['events'][0]['message']['longitude']
                        items[6] = payload['events'][0]['message']['latitude']

                        txtAppeal = ""
                        txtAppeal = txtAppeal+"\n- กรอกข้อมูลพิกัดเรียบร้อย\n"
                        txtAppeal = txtAppeal+"- ท่านสามารถแนบไฟล์ภาพเพื่่อเป็นหลักฐานเพิ่มได้\n"
                        txtAppeal = txtAppeal+"- กรุณาตรวจสอบข้อมูลก่อนบันทึก\n"
                        txtAppeal = txtAppeal+"- หากต้องการแก้ข้อมูลให้ทำการเลือกเมนู 'ร้องเรียน' อีกครั้ง\n"

                        sendQuickReplyManager(line_bot_api,replyToken,userId,txtAppeal) 
                else:
                    sendMessageManager(line_bot_api,replyToken,userId,"ท่านยังไม่ได้กรอกข้อมูลร้องเรียน")

        except Exception as e:
            return 200
            
    #กรณีผู้ใช้งานส่งข้อความเป็น image
    elif message_type == "image":
        try:
            #ทำกาบันทึกภาพที่ผู้ใช้งานส่งมา
            userId = payload['events'][0]['source']['userId']
            if userId in Buffer.items :
                message_id = payload['events'][0]['message']['id']
                file_path = "media/{}.png".format(message_id)
                message_content = line_bot_api.get_message_content(message_id)
                with open(file_path, 'wb') as fd:
                    for chunk in message_content.iter_content():
                        fd.write(chunk)

                if userId not in Buffer.images:
                    Buffer.images.update({userId: []})
                
                images = Buffer.images[userId]
                imageInfo = [message_id,file_path]
                images.append(imageInfo)

                txtAppeal = ""
                txtAppeal = txtAppeal+"\n- แนบภาพหลักฐานเรียบร้อย\n"
                txtAppeal = txtAppeal+"- ท่านสามารถแนบไฟล์ภาพเพื่่อเป็นหลักฐานเพิ่มได้\n"
                txtAppeal = txtAppeal+"- กรุณาตรวจสอบข้อมูลก่อนบันทึก\n"
                txtAppeal = txtAppeal+"- หากต้องการแก้ข้อมูลให้ทำการเลือกเมนู 'ร้องเรียน' อีกครั้ง\n"

                sendQuickReplyManager(line_bot_api,replyToken,userId,txtAppeal)
            else:
                sendMessageManager(line_bot_api,replyToken,userId,"ท่านยังไม่ได้กรอกข้อมูลร้องเรียน")
        except Exception as e:
            return 200
    
    #กรณีอื่นๆที่ไม่อยู่ในกรณีที่กำหนด
    else:
        printBufferStatus(True)
                
    return 200

def sendMessageManager(line_bot_api,replyToken,userId,message):
    try:
        ReplyTextMessage(line_bot_api,replyToken,message)
        printBufferStatus(False)
    except Exception as e:
        Buffer.pushMessageCount = Buffer.pushMessageCount + 1
        writePushMessageCount(str(Buffer.pushMessageCount))
        printBufferStatus(True)
        #line_bot_api.push_message(userId, TextSendMessage(text=message))

def sendQuickReplyManager(line_bot_api,replyToken,userId,message,iType=1):
    try:
        ReplyQuickButtons(line_bot_api,replyToken,message,iType)
        printBufferStatus(False)
    except Exception as e:
        Buffer.pushMessageCount = Buffer.pushMessageCount + 1
        writePushMessageCount(str(Buffer.pushMessageCount))
        printBufferStatus(True)
        #line_bot_api.push_message(userId, TextSendMessage(text=message))

def printBufferStatus(isException):
        if not isException :
            print("Number Of users : ", (len(Buffer.items)-1) ," , Number Of Images Owner : ",(len(Buffer.images)-1), "Number of pushMessage : ",Buffer.pushMessageCount)
        else:
            print("Number Of users : ", (len(Buffer.items)-1) ," , Number Of Images Owner : ",(len(Buffer.images)-1), "Number of pushMessage : ",Buffer.pushMessageCount,", isRedelivery = true, Invalid reply token")

def writePushMessageCount(message):
    file = open("custom/pushMessage.txt", "a")
    file.write(message)
    file.write('\n')
    file.close()