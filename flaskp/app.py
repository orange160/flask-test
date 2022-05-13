"""
@File  : app.py.py
@Author: lyj
@Create  : 2022/5/12 16:57
@Modify  : 2022/5/12 16:57
@Desc  : 
"""
from flask import Flask

import config
from flaskp.extensions import mail, celery


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    configure_app(app)
    configure_blueprints(app)
    configure_extensions(app)
    configure_celery_app(app, celery)

    return app


def configure_app(app):
    app.config.from_object(config)


def configure_blueprints(app):
    from flaskp.home import views as home_views
    app.register_blueprint(home_views.bp)


def configure_extensions(app):
    mail.init_app(app)


def configure_celery_app(app, celery_app):
    celery_app.config_from_object('celeryconfig')

    TaskBase = celery_app.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_app.Task = ContextTask
