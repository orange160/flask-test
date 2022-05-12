"""
@File  : views.py
@Author: lyj
@Create  : 2022/5/12 17:23
@Modify  : 2022/5/12 17:23
@Desc  : 
"""
import time

from flask import Blueprint

from flaskp.utils.mail_utils import send_mail

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def homepage():
    return '%s' % time.time()


@bp.route('/mail')
def home_send_mail():
    print('start to send mail')
    send_mail()
    print('send mail done')
    return '%s' % time.time()
