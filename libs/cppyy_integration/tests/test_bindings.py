# pytest/nosetest sanity test script.
import logging
import os
import pydoc
import subprocess
import sys


SCRIPT_DIR = os.path.dirname(__file__)
pkg = 'cppyy_integration'
PIPS = None


class TestBindings(object):
    @classmethod
    def setup_class(klass):
        #
        # Make an attempt to check the verbosity setting (ignore quiet!).
        #
        verbose = [a for a in sys.argv[1:] if a.startswith(('-v', '--verbos'))]
        if verbose:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
        else:
            logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    @classmethod
    def teardown_class(klass):
        pass

    def setUp(self):
        '''This method is run once before _each_ test method is executed'''

    def teardown(self):
        '''This method is run once after _each_ test method is executed'''

    def test_install(self):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--force-reinstall', '--pre', '.'], cwd=os.getcwd())

    def test_import(self):
        __import__(pkg)

    def test_help(self):
        pydoc.render_doc(pkg)

    def test_uninstall(self):
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '--yes', pkg], cwd=os.getcwd())

