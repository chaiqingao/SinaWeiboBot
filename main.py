from apscheduler.schedulers.blocking import BlockingScheduler

from weibo import WeiboClient
from func.FollowTVPlayFunc import FollowTVPlayFunc
from func.EnglishTodayFunc import EnglishTodayFunc
from func.PoetryFunc import PoetryFunc
import datetime

if __name__ == '__main__':
    client = WeiboClient('./data/WeiboClient.json')
    scheduler = BlockingScheduler()
    # follow_tv_play_fun = FollowTVPlayFunc(client, './data/西部世界第三季.json', '2736', '小小柴io')
    english_today_fun = EnglishTodayFunc(client, './data/EnglishToday.json')
    poetry_func = PoetryFunc(client, './data/Poetry.json')
    # scheduler.add_job(follow_tv_play_fun.do, 'interval', minutes=10, next_run_time=datetime.datetime.now())
    scheduler.add_job(english_today_fun.do, 'cron', hour=8)
    scheduler.add_job(poetry_func.do, 'cron', hour=18)
    print('Sina Weibo robot started successfully!')
    scheduler.start()
