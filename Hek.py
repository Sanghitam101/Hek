
import sys
import time
def slowprint(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./50)import sys
import time
def slowprint(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./50)

slowprint ("""
hallo word""")
