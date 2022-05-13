"""
@File  : mail_task.py
@Author: lyj
@Create  : 2022/5/13 11:17
@Modify  : 2022/5/13 11:17
@Desc  : 邮件后台任务
"""
import time

from flaskp.extensions import celery
from flask_mail import Message

import config
from flaskp.extensions import mail


@celery.task
def send_plaintext_mail(receivers, subject, text, attachments=None):
    """
    发送文本邮件
    :param receivers: 接收人邮箱，列表
    :param subject: 邮件主题
    :param text: 邮件消息
    :param attachments: 附件
    :return:
    """
    # if attachments is None:
    #     attachments = []
    # msg = Message(subject,
    #               sender=(config.SYSTEM_NAME, config.MAIL_USERNAME),
    #               recipients=receivers)
    # msg.body = text
    # mail.send(msg)
    print('send mail doing')
    time.sleep(2)


@celery.task
def send_html_mail(receivers, subject, html_doc, attachments=None):
    """
    发送html邮件
    :param receivers: 接收人邮箱，列表
    :param subject: 邮件主题
    :param html_doc: 邮件消息
    :param attachments: 附件
    :return:
    """
    if attachments is None:
        attachments = []
    msg = Message(subject,
                  sender=(config.SYSTEM_NAME, config.MAIL_USERNAME),
                  recipients=receivers)
    msg.html = html_doc
    mail.send(msg)
