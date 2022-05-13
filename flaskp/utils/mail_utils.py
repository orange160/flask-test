"""
@File  : mail_utils.py
@Author: lyj
@Create  : 2022/5/12 17:40
@Modify  : 2022/5/12 17:40
@Desc  : 
"""
from flask_mail import Message

import config
from flaskp.extensions import mail


def send_mail():
    """
    邮件配置
    MAIL_SERVER = 'smtp.yeah.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'your email'
    MAIL_PASSWORD = 'your email password'
    MAIL_DEFAULT_SENDER = 'your email'
    MAIL_DEBUG = 0  # 0--关闭调试 1--开启调试
    """
    msg = Message("Hello",
                  sender=('MMao', config.MAIL_USERNAME),
                  recipients=["lyjorange2019@126.com"])
    msg.html = "<b>testing</b>"
    mail.send(msg)
