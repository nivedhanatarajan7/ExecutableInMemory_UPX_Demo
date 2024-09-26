import os

def create_exe(filename):
    os.popen("pyinstaller --onefile --console " + filename+ ".py")

    return ("./dist/" + filename + ".exe")