
from application import app, db, manager
from www import *
from flask_script import Server, Command
from jobs.launcher import runJob

manager.add_command( 'runserver', Server(host = '127.0.0.1', use_debugger=True, use_reloader=True))
manager.add_command("runJob", runJob)

@Command
def create_all():
    from application import db
    from common.models.user import User
    db.create_all()

manager.add_command('create_all', create_all)


def main():
    manager.run()
if __name__=='__main__':

    #app.run(debug=True)
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()