import requests
import json

from func.Func import Func


class EnglishTodayFunc(Func):
    def __init__(self, client, data_path):
        super().__init__(client, data_path, {})

    def func(self):
        res = json.loads(requests.get('http://open.iciba.com/dsapi/').text)
        status = res['content'] + '\n' + res['note']
        pic = res['picture4']
        self.client.post(status=status, pic=pic)
        self.log('Successfully post!')
