#encoding: utf-8
from flask_script import Command
import sys, argparse, traceback, importlib


class runJob(Command):

    capture_all_args = True
    def run(self, *args, **kwargs):
        args = sys.argv[2:]
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("-m", '--name', dest="name", metavar="name", help="Point out job name", required=True)
        parser.add_argument("-a", '--act', dest="act", metavar="act", help="Point out job action", required=False)
        parser.add_argument("-p", '--param', dest="param", metavar="param", nargs="*", help="Point out job name", required=False)
        params = parser.parse_args(args)
        params_dict = params.__dict__
        if "name" not in params_dict or not params_dict['name']:
            return self.tips()

        try:
            module_name = params_dict['name'].replace('/', '.')
            import_string = 'jobs.tasks.{}'.format(module_name)
            target = importlib.import_module(import_string)
            exit(target.JobTask().run(params_dict))
        except Exception as e:
            traceback.print_exc()
        return

    def tips(self):
        tip_msg = '''
        Please input the correct job name
        python manager.py runJob -m Test
        python manger.py runJob -m test/index
        '''
        print(tip_msg)
        return