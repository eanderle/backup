import subprocess
from os.path import expanduser

print subprocess.check_output(['gmvault', 'sync', 'enanderle@gmail.com', '-d', expanduser('~/backup/gmail/enanderle')])
