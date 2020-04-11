from apscheduler.schedulers.blocking import BlockingScheduler

from weibo import WeiboClient
from func.FollowTVPlayFunc import FollowTVPlayFunc
from func.EnglishTodayFunc import EnglishTodayFunc
from func.PoetryFunc import PoetryFunc

if __name__ == '__main__':
    with open('./data/access_token.txt', 'rt') as f:
        access_token = f.read()
    client = WeiboClient(access_token)
    scheduler = BlockingScheduler()
    follow_tv_play_fun = FollowTVPlayFunc(client, './data/西部世界第三季.json', '2736', '小小柴io')
    english_today_fun = EnglishTodayFunc(client, './data/EnglishToday.json')
    poetry_func = PoetryFunc(client, './data/Poetry.json')
    scheduler.add_job(follow_tv_play_fun.do, 'interval', minutes=10)
    scheduler.add_job(english_today_fun.do, 'interval', days=1, start_date='2020-4-12 08:00:00')
    scheduler.add_job(poetry_func.do, 'interval', days=1, start_date='2020-4-12 18:00:00')
    scheduler.start()
