from controllers.index import index_page
from application import app
from flask_debugtoolbar import DebugToolbarExtension
from controllers.member import member_page
toolbar = DebugToolbarExtension(app)

app.register_blueprint(index_page, url_prefix = '/')
app.register_blueprint(member_page, url_prefix = '/member')

from interceptors.Auth import *
from interceptors.errorsHunter import *

from common.libs.urlManager import urlManager
app.add_template_global( urlManager.buildStaticURL, 'buildStaticURL')
app.add_template_global( urlManager.buildURL, 'buildURL')