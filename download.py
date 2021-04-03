import os 
import sys
import subprocess


for i in os.listdir(r"C:\Users\NickQuinnPro\Documents\Projects\Test\requirement"):
    x = str(i)
    if x.endswith('.whl') or x.endswith('.gz'):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', x, '-f', './', '--no-index', '--no-deps'])