from application import app
from common.libs.DataHelper import getCurrentTime
import os
class urlManager(object):
    @staticmethod
    def buildURL(path):
        config_domain = app.config['DOMAIN']
        return '{}{}'.format(config_domain['www'], path)

    @staticmethod
    def buildStaticURL(path):
        path = '/static' + path + '?ver=' + urlManager.getReleaseVersion()
        return urlManager.buildURL(path)

    @staticmethod
    def getReleaseVersion():
        ver = '{}'.format(getCurrentTime("%Y%m%d%H%M%S%f"))
        release_path = app.config.get('RELEASE_PATH')
        if release_path and os.path.exists(release_path):
            with open(release_path, 'r') as f:
                ver = f.readline()
        return ver