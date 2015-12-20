import subprocess
import sys
#p = subprocess.Popen (['python','../pi-code/lcd4/mm/message.py',sys.argv[1]])
p = subprocess.Popen (['python','scrollOLED.py',sys.argv[1]])
print "starting process "+str(p.pid)
