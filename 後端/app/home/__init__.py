from flask import Blueprint

api = Blueprint("app",__name__)

# 導入藍圖的視圖
from . import hotels