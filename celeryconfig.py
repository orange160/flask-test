"""
@File  : celeryconfig.py
@Author: lyj
@Create  : 2022/4/8 11:12
@Modify  : 2022/4/8 11:12
@Desc  : 
"""
# celery
from datetime import timedelta

from celery.schedules import crontab

import config

broker_url = config.REDIS_URL
result_backend = config.REDIS_URL

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True

# celery redbeat
redbeat_redis_url = config.REDIS_URL
redbeat_key_prefix = 'redbeat'

# 导入任务所在文件
imports = [
    'flaskp.tasks.schedule_task'
]

beat_schedule = {
    # 每 30秒执行一次。 秒级别可以用 timedelta, 分钟级别及以上可以用 crontab
    'schedule-task': {
        'task': 'flaskp.tasks.schedule_task.schedule_common',
        'schedule': timedelta(seconds=20),
        'args': ()
    }
}
