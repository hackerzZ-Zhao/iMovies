# coding: utf-8
from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='主键')
    nickname = db.Column(db.String(30), nullable=False, unique=True, server_default=db.FetchedValue(), info='昵称')
    login_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='用户名')
    login_pwd = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='用户密码')
    login_salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='盐')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0无效1有效')
    updated_time = db.Column(db.DateTime, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
