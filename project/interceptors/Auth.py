from application import app
from flask import request, g
from common.models.user import User
from common.libs.UserService import UserService


@app.before_request
def before_request():
    app.logger.info('111')
    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
    return

@app.after_request
def after_request(response):
    app.logger.info('222')
    return response

def check_login():
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    auth_cookie = cookies[cookie_name] if cookie_name in cookies else None
    if not auth_cookie:
        return False

    auth_info = auth_cookie.split('#')
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if not user_info:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    return user_info