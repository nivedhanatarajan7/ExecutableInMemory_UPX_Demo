import os
import subprocess

def run_exe(path):
    os.popen("upx --force " + path)

    subprocess.run(path)