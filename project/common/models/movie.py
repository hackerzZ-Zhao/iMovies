# coding: utf-8
from application import db

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='电影名称')
    classify = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='类别')
    actor = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='主演')
    cover_pic = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='封面图')
    pics = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='图片地址json')
    url = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='电影详情地址')
    desc = db.Column(db.Text, nullable=False, info='电影描述')
    magnet_url = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='磁力下载地址')
    hash = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue(), info='唯一值')
    pub_date = db.Column(db.DateTime, nullable=False, index=True, info='来源网址发布日期')
    source = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='来源')
    view_counter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阅读数')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])