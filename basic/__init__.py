from flask import Flask, request, abort,jsonify
from flask_autoindex import AutoIndex

from custom.Config import *
from custom.WebhookManager import *

from custom.PublicURL import public_root_url

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)

app = Flask(__name__)
AutoIndex(app, browse_root=ROOT_MEDIA_PATH)  

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route(WEBHOOK_ROOT, methods=['POST'])
def webhook():
    try:
        payload = request.json
        manage(line_bot_api,payload)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return "OK",200

#example : http://127.0.0.1:5000/images?message_id=17734042748891
@app.route(IMAGES_ROOT, methods=['POST','GET'])
def images():
    message_id = "None"
    if request.method == 'POST':
        message_id = request.form.get('message_id')
    else:
        message_id = request.args.get('message_id')

    import base64
    encoded_string = "None"
    file_path = "media/{}.png".format(message_id)
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string,200

#example for select all : http://127.0.0.1:5000/appeals?key=&val=&isLike=no
#example for filter : http://127.0.0.1:5000/appeals?key=id&val=5&isLike=no
#example for like : http://127.0.0.1:5000/appeals?key=personName&val=ภูมิพัฒน์&isLike=yes
@app.route("/appeals", methods=['POST','GET'])
def appeals():

    aClause = ""
    key = ""
    val = ""
    isLike = "no"

    if request.method == 'POST':
        key = request.form.get('key')
        val = request.form.get('val')
        isLike = request.form.get('isLike')
    else:
        key = request.args.get('key')
        val = request.args.get('val')
        isLike = request.args.get('isLike')

    if key != "" and val != "" and isLike =="no":
        aClause = str(key)+"='"+str(val)+"'"
    elif key != "" and val != "" and isLike =="yes":
        aClause = str(key)+" like '%"+str(val)+"%'"

    import json
    from db.appeal import AppealInfo
    appeals_dict = []
    appeals = AppealInfo()
    results = appeals.Select(aClause)
    for row in results:
        appeals_dict.append({"id":row[0],"userId":row[1],"displayName":row[2],"personName":row[3],"detail":row[4],"progress":row[5],"lon":row[6],"lat":row[7],"unit":row[8],"updateDate":row[9]})

    json_results = json.dumps(appeals_dict, ensure_ascii=False).encode('utf8')
    return json_results.decode(),200


#example for select all : http://127.0.0.1:5000/appeals?key=&val=&isLike=no
#example for filter : http://127.0.0.1:5000/appeals?key=id&val=5&isLike=no
#example for like : http://127.0.0.1:5000/appeals?key=personName&val=ภูมิพัฒน์&isLike=yes

@app.route("/appealsCsv", methods=['POST','GET'])
def appealsCsv():

    aClause = ""
    key = ""
    val = ""
    isLike = "no"

    if request.method == 'POST':
        key = request.form.get('key')
        val = request.form.get('val')
        isLike = request.form.get('isLike')
    else:
        key = request.args.get('key')
        val = request.args.get('val')
        isLike = request.args.get('isLike')

    if key != "" and val != "" and isLike =="no":
        aClause = str(key)+"='"+str(val)+"'"
    elif key != "" and val != "" and isLike =="yes":
        aClause = str(key)+" like '%"+str(val)+"%'"

    file_path = "media/appeals.csv"
    import csv
    from db.appeal import AppealInfo
    appeals = AppealInfo()
    results = appeals.Select(aClause)

    column_names = [i[0] for i in appeals.getColumnNames().description]

    fp = open(file_path, 'w')
    myFile = csv.writer(fp, lineterminator = '\n')
    myFile.writerow(column_names)
    myFile.writerows(results)
    fp.close()

    root_url = public_root_url()
    public_url = root_url.get_public_url()

    return str(public_url)+"/appeals.csv",200
    