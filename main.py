from weibo import WeiboClient
from func.zjfunc import ZjFunc
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    with open('./data/access_token.txt', 'rt') as f:
        access_token = f.read()
    client = WeiboClient(access_token)
    scheduler = BlockingScheduler()
    zjfun = ZjFunc(client, './data/西部世界第三季.json', '2736', '小小柴io')
    scheduler.add_job(zjfun.do, 'interval', minutes=10)
    scheduler.start()
