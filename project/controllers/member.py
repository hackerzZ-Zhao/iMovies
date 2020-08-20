from application import app, db
from flask import Blueprint, render_template, request, make_response, redirect
from common.libs.DataHelper import getCurrentTime
from common.libs.urlManager import urlManager
from common.libs.Helper import *
from common.models.user import User
from common.libs.UserService import UserService


member_page = Blueprint('member_page', __name__)
@member_page.route('/reg', methods = ["GET", 'POST'])
def reg():
    if request.method == 'GET':
        return ops_render('member/reg.html')

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    login_pwd2 = req['login_pwd2'] if 'login_pwd2' in req else ''

    if not login_name or len(login_name) < 1:
        return ops_renderErrJSON(msg="Please input correct username!")

    if not login_pwd or len(login_pwd) < 6:
        return ops_renderErrJSON(msg="Please input correct password! At least 6 characters!")

    if login_pwd != login_pwd2:
        return ops_renderErrJSON(msg="Password not match!Please check and input again!")

    user_info = User.query.filter_by(login_name = login_name).first()
    if user_info:
        return ops_renderErrJSON(msg="Username already exist!")

    model_user = User()
    model_user.login_name = login_name
    model_user.nickname = login_name
    model_user.login_salt = UserService.genSalt(8)
    model_user.login_pwd = UserService.genePwd(login_pwd, model_user.login_salt)
    model_user.created_time = model_user.updated_time = getCurrentTime()
    db.session.add(model_user)
    db.session.commit()
    return ops_renderJSON(msg="Register Success!")


@member_page.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        return ops_render('member/login.html')

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if not login_name or len(login_name) < 1:
        return ops_renderErrJSON(msg="Please input correct username!")

    if not login_pwd or len(login_pwd) < 6:
        return ops_renderErrJSON(msg="Please input correct password! At least 6 characters!")

    user_info = User.query.filter_by(login_name = login_name).first()
    if not user_info:
        return ops_renderErrJSON("Please input correct username and password!")

    if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
        return ops_renderErrJSON("Please input correct username and password!")

    if user_info.status != 1:
        return ops_renderErrJSON("Account has been forbidden!")

    #session['uid'] = user_info.id
    response = make_response(ops_renderJSON(msg="Success!"))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                       '{}#{}'.format(UserService.geneAuthCode(user_info), user_info.id), 60 * 60 * 24 * 120)
    return response

@member_page.route("/logout")
def logout():
    response = make_response(redirect(urlManager.buildURL('/')))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response