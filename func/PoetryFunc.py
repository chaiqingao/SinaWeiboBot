import requests
import json

from func.Func import Func


class PoetryFunc(Func):
    def __init__(self, client, data_path):
        super().__init__(client, data_path, {'token': ''})
        self.get_token()

    def func(self):
        if self.data['data']['token'] == '':
            self.error('token is ""!')
            return
        res = json.loads(requests.get('https://v2.jinrishici.com/sentence',
                                      cookies={'X-User-Token': self.data['data']['token']}).text)
        data = res['data']
        sentence = data['content']
        origin = data['origin']
        title = origin['title']
        dynasty = origin['dynasty']
        author = origin['author']
        content = origin['content']
        status = '{}\n语出《{}》【{}】{}'.format(sentence, title, dynasty, author)
        self.client.post(status=status)
        self.log('Successfully post!')

    def get_token(self):
        if self.data['data']['token'] == '':
            try:
                res = json.loads(requests.get('https://v2.jinrishici.com/token').text)
                self.data['data']['token'] = res['data']
            except Exception as e:
                self.data['error'] = str(e)
            self.save_data()
            self.load_data()
