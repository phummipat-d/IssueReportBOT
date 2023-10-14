import ngrok
import json
import requests
from custom.Config import *

def updateWebHook():
    client = ngrok.Client(NGROK_TOKEN_API)
    # List all online tunnels
    
    for line in client.tunnels.list():
        if(line.forwards_to == LOCAL_HOST_URL):
            
            #public_root_url.url = line.public_url
            writeWebhookURL(line.public_url)

            payload = json.dumps({"endpoint": line.public_url + WEBHOOK_ROOT})
            headers = {
                'Authorization': 'Bearer {}'.format(CHANNEL_ACCESS_TOKEN),
				'Content-Type': 'application/json'
			}

            updatewebhookurl = requests.request("PUT", LINE_WEBHOOK_API, headers=headers, data=payload)
            if updatewebhookurl.status_code == 200:
                print("Update webhook url success!")
            else:
                print("Something went wrong!")

def writeWebhookURL(public_url):
    file = open("custom/webhookURL.txt", "w")
    file.write(public_url)
    file.close()