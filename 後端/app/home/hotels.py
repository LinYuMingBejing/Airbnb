from . import api

@api.route("/123")
def home():
    return "<div>123123</div>"