"""
@File  : schedule_tasks.py
@Author: lyj
@Create  : 2022/5/13 14:54
@Modify  : 2022/5/13 14:54
@Desc  : 
"""
from flaskp.extensions import celery
from flaskp.tasks.mail_task import send_plaintext_mail


@celery.task
def schedule_common():
    print('start to send mail')
    # send_plaintext_mail.delay(['lyjorange2019@126.com'], 'this is a test email', 'this is content text')
    print('send mail done')
