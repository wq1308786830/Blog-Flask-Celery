#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
from importlib import reload

__author__ = 'Russell'

reload(sys)

WEIXIN_DEBUG = False
DEBUG = not os.path.exists("/var/www/xmjdw")

# Mysql
if DEBUG:
    """
        开发模式的配置项
    """
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB = 'test'

    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'

    APNS_KEY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'system/apns-test.pem')

    print('====================启动开发者模式========================')

else:
    """
        生产环境的配置项
    """
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB = 'test'

    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'

    APNS_KEY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'system/apns.pem')

    print('=======================启动生产环境模式=============================')

"""
    通用配置
"""
VERIFY_EMAIL = False
JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "flskt19472kfirdibofneictoqKDIVME"

MIPUSH_SECRET = "WaaQ+3EWcOE63Dg0Gbs4AQ=="
