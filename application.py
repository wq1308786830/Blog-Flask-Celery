# -*- coding: utf-8 -*-
# !/usr/bin/python

import os

from flask import Flask, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from apps.tasks import make_celery

PROJECT_PATH = os.path.dirname(__file__)

db = SQLAlchemy()


def config_log(app):
    import logging
    from logging.handlers import RotatingFileHandler

    format = '[%(asctime)s %(levelname)s]: %(message)s [in %(pathname)s:%(lineno)d]'
    log_file = app.config.get("LOG_FILE")
    if log_file:
        handler = RotatingFileHandler(
            log_file,
            maxBytes=10000,
            backupCount=10,
        )
        handler.setFormatter(logging.Formatter(format))
        app.logger.addHandler(handler)

    debug = app.debug
    if not debug:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(format))
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.WARN)

    app.logger.warn("logging is ready")


def config_db(app):
    """
    配置数据库session创建
    :param app:
    :return:
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + app.config['MYSQL_USER'] + ':' + \
                                            app.config['MYSQL_PASS'] + '@' + app.config['MYSQL_HOST'] + ':' + \
                                            app.config['MYSQL_PORT'] + '/' + app.config['MYSQL_DB']


def config_route(app):
    """
    配置 url
    :param app:
    :return:
    """
    common_prefix = ''
    from apps.blogs import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix=common_prefix)

    @app.errorhandler(400)
    def handler_400(error):
        return json.dumps(dict(message='参数不能为空:' + str(error.args))), 400


def config_celery(app):
    """

    :param app:
    :return:
    """
    make_celery(app)


def create_app():
    app = Flask(__name__)
    CORS(app)
    config_file = os.path.abspath(os.path.join(PROJECT_PATH, 'etc/config.py'))

    app.config.from_pyfile(config_file)
    config_celery(app)
    config_log(app)
    config_db(app)
    config_route(app)
    db.init_app(app)

    app.logger.info("app准备好了")

    return app
