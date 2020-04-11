import requests
from bs4 import BeautifulSoup

from func.Func import Func


class FollowTVPlayFunc(Func):
    def __init__(self, client, data_path, code, weibo_id):
        super().__init__(client, data_path, {'text': ''})
        self.code = code
        self.weibo_id = weibo_id
        self.ROOT_URL = 'https://www.zxzj.me'
        self.DETAIL_URL = self.ROOT_URL + '/detail/' + self.code

    def func(self):
        text_last = self.data['data']['text']
        r = requests.get(self.DETAIL_URL, timeout=5)
        html = BeautifulSoup(r.text, 'lxml')
        pic = html.find_all('img', {'class': 'lazyload'})[0].attrs['data-original']
        title = html.find_all('h1')[0].text
        a = html.find_all('ul', {'class': 'stui-content__playlist clearfix'})[0].find_all('li')[-1].find('a')
        text = a.text
        url = self.ROOT_URL + a.attrs['href']
        self.data['data']['text'] = text
        if text != text_last:
            self.client.post(status='@{} 你关注的{}更新至{}了，视频链接：{}'.
                             format(self.weibo_id, title, text, url), pic=pic)
            self.log('Successfully post!')
