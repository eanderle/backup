import subprocess
from os.path import expanduser

subprocess.call(['python', './drive.py', '--destination', expanduser('~/backup/gdrive/')])
print subprocess.check_output(['ls', '-l', expanduser('~/backup/gdrive/My Drive')])
