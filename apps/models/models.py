# coding=utf-8
# !/usr/bin/python

from application import db


# 创建对象的基类:
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))
    # 一对多:
    books = db.relationship('Book')

    def __repr__(self):
        return '<User %r>' % self.name

    @staticmethod
    def add_user(user_name, user_id):
        # 创建session对象:
        session = db.session()
        if not session.query(User).filter(User.id == user_id):
            print(user_name, user_id)
            # 创建新User对象:
            new_user = User(id=user_id, name=user_name)
            # 添加到session:
            session.add(new_user)
        # simple query
        user = session.query(User).filter(User.name == 'a').first()
        print(user.id + user.name)
        # 提交即保存到数据库:
        session.commit()


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Book %r>' % self.name

