from abc import ABCMeta, abstractmethod
import json
from datetime import datetime


class Func(metaclass=ABCMeta):
    def __init__(self, client, data_path, fun_data):
        self.client = client
        self.data_path = data_path
        self.data = {
            'data': fun_data,
            'error': '',
            'update_time': ''
        }
        try:
            self.load_data()
        except Exception as e:
            self.data['error'] = str(e)
            self.save_data()

    @abstractmethod
    def func(self):
        pass

    def do(self):
        try:
            self.load_data()
            self.func()
        except Exception as e:
            self.data['error'] = str(e)
        self.save_data()

    def load_data(self):
        with open(self.data_path, 'rt') as f:
            tmp = json.load(f)
        if tmp.get('update_time') is None or tmp.get('data') is None:
            raise Exception('Wrong data format!')
        self.data = tmp
        self.data['error'] = ''

    def save_data(self):
        self.data['update_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.data_path, 'wt') as f:
            json.dump(self.data, f)

    def log(self, info):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Time: {}, {}: {}'.format(time, self.__class__.__name__, info))

    def error(self, error):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('\033[1;31mTime: {}, {}: {}\033[0m'.format(time, self.__class__.__name__, error))
