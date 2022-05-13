#!/usr/bin/env python

from flaskp.app import create_app
from flaskp.extensions import celery  # noqa

app = create_app()
