# -*- coding: utf-8 -*-
# !/usr/bin/python

from flask import render_template

from application import db
from apps.models.models import User
from . import blog

__author__ = 'Russell'


@blog.route("/")
def index():
    """

    :return:
    """

    return render_template("index.html")


@blog.route("/<user_id>&<user_name>")
def add_query(user_id, user_name):
    """

    :param user_id:
    :param user_name:
    :return:
    """

    # User.add_user(user_id, user_name)
    user = User(id=user_id, name=user_name)
    db.session.add(user)
    db.session.commit()
    return render_template("index.html")


@blog.route('/run_girl')
def run_girl():
    """
    svg跑步的小女孩
    :return:
    """
    return render_template('bezier_running_girl.html')
