# SinaWeiboBot
新浪微博机器人

demo: [@追更bot](https://weibo.com/u/7429317732)（部署在一块树莓派上）

## 依赖

- Python3
- requests
- bs4
- APScheduler

## 下载安装

```shell script
git clone https://github.com/chaiqingao/SinaWeiboBot.git
cd SinaWeiboBot
pip install -r requirements.txt
```

## 准备工作

1. 在[微博开放平台](https://open.weibo.com)创建移动应用
2. 填写应用基本信息，安全域名必填（发送微博时须附上）
3. 打开[API测试工具](https://open.weibo.com/tools/console/)，复制`Access Token`并保存至文件`data/access_token.txt`

## 任务设置

打开`main.py`，设置方法如下：

### 追更任务

```python
# 2736为西部世界第三季的id*，小小柴io为发微博要提醒的人
follow_tv_play_fun = FollowTVPlayFunc(client, './data/西部世界第三季.json', '2736', '小小柴io')
# minutes为执行间隔，可以根据需要设置
scheduler.add_job(follow_tv_play_fun.do, 'interval', minutes=10)
```

*注：id从[在线之家](https://www.zxzj.me)获取

### 每日诗词任务

```python
poetry_func = PoetryFunc(client, './data/Poetry.json')
# 定时任务，每日8点执行
scheduler.add_job(poetry_func.do, 'cron', hour=8)
```

### 每日一句任务
```python
english_today_fun = EnglishTodayFunc(client, './data/EnglishToday.json')
# 定时任务，每日18点执行
scheduler.add_job(english_today_fun.do, 'cron', hour=18)
```

有关定时任务的更多设置方式请参见[Advanced Python Scheduler](https://apscheduler.readthedocs.io/en/stable/)

## 启动

```shell script
python main.py
```

## To Do
- [ ] 长文字转图片，以便发送长微博
