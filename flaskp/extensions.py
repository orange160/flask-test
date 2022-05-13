"""
@File  : extensions.py
@Author: lyj
@Create  : 2022/5/12 17:22
@Modify  : 2022/5/12 17:22
@Desc  : 
"""
from celery import Celery
from flask_caching import Cache
from flask_mail import Mail

# 邮件
from flask_redis import FlaskRedis

import celeryconfig

mail = Mail()

# Redis
redis_store = FlaskRedis()

# Caching
cache = Cache()

# Celery
celery = Celery("flaskp", broker=celeryconfig.broker_url)
