import requests
from bs4 import BeautifulSoup

from func.Func import Func


class FollowTVPlayFunc(Func):
    def __init__(self, client, data_path, code, weibo_ids):
        super().__init__(client, data_path, {'text': ''})
        self.code = code
        self.weibo_ids = weibo_ids
        self.ROOT_URL = 'https://www.zxzj.me'
        self.DETAIL_URL = self.ROOT_URL + '/detail/' + self.code

    def func(self):
        text_last = self.data['data']['text']
        r = requests.get(self.DETAIL_URL, timeout=5)
        index = r.text.find('?btwaf=')
        if index != -1:
            r = requests.get(self.DETAIL_URL + r.text[index:index+15], timeout=5)
        html = BeautifulSoup(r.text, 'lxml')
        pic = html.find_all('img', {'class': 'lazyload'})[0].attrs['data-original']
        title = html.find_all('h1')[0].text
        a = html.find_all('ul', {'class': 'stui-content__playlist clearfix'})[0].find_all('li')[-1].find('a')
        text = a.text
        url = self.ROOT_URL + a.attrs['href']
        self.data['data']['text'] = text
        if text != text_last:
            at = ''.join(list(map(lambda x: '@'+x+' ', self.weibo_ids)))
            self.client.post(status='{} 你{}关注的{}更新至{}了，视频链接：{}'.
                             format(at, '们' if len(self.weibo_ids) > 1 else '', title, text, url), pic=pic)
            self.log('Successfully post!')
