from flask_sqlalchemy import SQLAlchemy
from app import db


class Hotel(db.Model):
    __tablename__='hotel'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(128),unique=True,nullable=False)
    category = db.Column(db.String(128))
    address = db.Column(db.String(128))
    score = db.Column(db.Integer,nullable=False)
    count = db.Column(db.Integer,nullable=False)
    image = db.Column(db.String(5024))
    landlord_img = db.Column(db.String(1024))
    house_info = db.Column(db.String(2048))
    secnery_list = db.Column(db.String(1024))
    secnery_list2 = db.Column(db.String(1024))
    comment_list = db.Column(db.String(4096))
    go_time = db.Column(db.String(24))
    exit_time = db.Column(db.String(24))
    facility = db.Column(db.String(256))
    room_type = db.Column(db.String(1024))
    prohibit = db.Column(db.String(256))

