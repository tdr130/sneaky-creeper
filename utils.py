'''
Holds utility functions for sneaky-creeper.
'''

import pip
import importlib
import os
import subprocess

def importModule(moduleName, quiet=True):
    # helper function to import a module, check
    # its dependencies, install if required, then
    # return the module
    mod = importlib.import_module(moduleName)
    # install dependencies
    try:
        for dep in mod.dependencies:
            if quiet:
                pip.main(['install', dep])
                #pip.main(['install', dep, '-q'])
            else:
                pip.main(['install', dep])
    except AttributeError:
        print("ERROR: module '{}' has no dependencies array.".format(mod.__file__))
        return False
    return mod

def venvMe(venvName):
    # save the dir we're in
    #origdir = os.getcwd()
    # change to this file's directory
    basedir = os.path.dirname(os.path.abspath(__file__))
    #os.chdir(basedir)
    # if there's a virtualenv, activate it
    activate_this = os.path.abspath(venvName + '/bin/activate_this.py')
    if not os.path.exists(activate_this):
        # if there isn't, create one
        try:
            subprocess.check_call(['virtualenv',venvName])
        except subprocess.CalledProcessError as e:
            # or at least try. Change back to old dir
            os.chdir(origdir)
            return False

    execfile(activate_this, dict(__file__=activate_this))
    # change back to old dir
    #os.chdir(origdir)
    return True