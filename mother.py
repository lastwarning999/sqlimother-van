import requests
import argparse


class cyberdetails:
    def __init__(self, token, chatIDs=[]):
        self.chatIDs = chatIDs
        self.token = token
        self.url = "https://api.telegram.org/bot"

        self.parser = argparse.ArgumentParser(description="github.com/ferhatcil")
        self.parser.add_argument('--name', required=False)
        self.args = self.parser.parse_args()

    def IFoundAnSql(self):
        for i in self.chatIDs:
            text = "<b>Congratulations! You found an sqli</b>%0A<i>{}</i>".format(self.args.name)
            url = self.url + self.token + "/sendMessage?chat_id={}&text={}&parse_mode=Html".format(i, text)
            requests.get(url)


app = cyberdetails("7077569483:AAHfdJIL77Y4L4Bz9iyQqw9eZ4pDKaDGOXk", ['6829567767'])
app.IFoundAnSql()
