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
    msg = Message("Hello",
                  sender=('MMao', config.MAIL_USERNAME),
                  recipients=["lyjorange2019@126.com"])
    msg.html = "<b>testing</b>"
    mail.send(msg)
