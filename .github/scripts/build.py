import sys
import os
from os import path
import subprocess

print("Checkout submodules")
subprocess.check_call(['git','submodule','update','--init','--recursive'])

BUILD_DIR = path.join('..','build_release')

print("Make sure the build directory exists")
if path.exists(BUILD_DIR) == False:
    os.mkdir(BUILD_DIR)

print("Pre-build")
if sys.platform.startswith('linux'):
    subprocess.check_call(['python','build_files/build_environment/install_linux_packages.py'])
    subprocess.check_call(['python','build_files/utils/make_update.py --use-linux-libraries'])

if sys.platform.startswith('darwin'):
    print("skip")
    sys.exit(0)
    subprocess.check_call(['xcode-select','--install'])
    subprocess.check_call(['brew','install','cmake git git-lfs svn'])

print("Build Blender project")
subprocess.check_call(['make.bat'])
subprocess.check_call(['ls'])
