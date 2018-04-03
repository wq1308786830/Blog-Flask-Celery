# -*- coding: utf-8 -*-
# !/usr/bin/python
import json
import os
from flask import render_template, request
from werkzeug import secure_filename
from application import db
from apps.models.models import User
from flask import Blueprint

__author__ = 'Russell'

blog = Blueprint('blog', __name__)

IMG_SERVER = 'http://http://104.156.250.95:7001/'
BLOG_IMG_UPLOAD_FOLDER = 'static/uploads/blog_images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


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


@blog.route('/1.0/manage/uploadBlgImg', methods=['GET', 'POST'])
def upload_blg_img():
    """
    receive blog editor's uploaded image.
    :return:
    """
    filename = None
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(BLOG_IMG_UPLOAD_FOLDER, filename))
    return json.dumps({'success': True, 'data': {'link': IMG_SERVER + BLOG_IMG_UPLOAD_FOLDER + filename}})


@blog.route('/run_girl')
def run_girl():
    """
    svg running girl
    :return:
    """
    return render_template('bezier_running_girl.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
