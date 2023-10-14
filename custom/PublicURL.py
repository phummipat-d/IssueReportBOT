from custom.Config import *
class public_root_url:
    url = "http://localhost:{}".format(PORT)
    def get_public_url(self):
        try:
            f = open("custom/webhookURL.txt", "r")
            self.url = "{}".format(f.read())
        except Exception as e:
            print(str(e))
        return self.url