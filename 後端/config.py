import os
import redis

class Config(object):
    """配置信息"""
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # 數據庫
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URI") or "mysql+pymysql://root:a828215362@localhost:3306/hotel"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST="127.0.0.1"
    REDIS_PORT = 6379

    # flask-session
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port = REDIS_PORT)
    SESSION_USE_SIGNER = True # 對cookie中session_id 進行隱藏處理
    PERMANENT_SESSION_LIFETIME = 86400 # session數據的有效期, 單位秒

class DevelopmentConfig(Config):
    """開發模式的配置信息"""
    DEBUG = True

class ProductConfig(object):
    """生產環境配置信息"""
    pass


config_map = {
    "develop":DevelopmentConfig,
    "product":ProductConfig
}