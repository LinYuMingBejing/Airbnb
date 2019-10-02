from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
from config import config_map


import redis
# 數據庫
db = SQLAlchemy()


# 創建redis連接對象
redis_store = None


# 工廠模式
def create_app(config_name):
    """
    創建flask的應用對象
    :params config_name: str 配置模式的名字 ("develop", "product")
    :return:
    """
    app = Flask(__name__)

    # 根據配置模式名字獲取配置參數的類
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port = config_class.REDIS_PORT)

    # 利用flask-session,將session數據保存到redis中
    Session(app)

    # 為flask補充csrf防護
    CSRFProtect(app)

    from .home import api as home_blueprint
    # 註冊藍圖
    app.register_blueprint(home_blueprint)
    return app