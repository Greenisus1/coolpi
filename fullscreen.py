import subprocess
from terminal_ui import run
def session(ui):
 ui.external(lambda:subprocess.run(['bash','controls-fullscreen.sh'],check=False))
if __name__=='__main__':raise SystemExit(run('CoolPi',session))
