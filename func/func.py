from abc import ABCMeta, abstractmethod
import json


class Func(metaclass=ABCMeta):
    def __init__(self, client, data_path, data):
        self.client = client
        self.data_path = data_path
        self.data = data
        try:
            self.load_data()
        except Exception as e:
            self.save_data()

    @abstractmethod
    def do(self):
        pass

    def load_data(self):
        with open(self.data_path, 'rt') as f:
            self.data = json.load(f)

    def save_data(self):
        with open(self.data_path, 'wt') as f:
            json.dump(self.data, f)
