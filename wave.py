#!/home/pi/say/say/bin/python3

import subprocess, sys, time, os.path
import urllib.request, urllib.parse
URL = # http://SERVER_URL_HERE:9997/?

def synth(z):
    r = urllib.request.urlopen(URL + urllib.parse.quote(z))
    assert r.headers['content-type'] == "audio/x-wav"
    return r.read()

if __name__ == "__main__":
    i = 0
    for text in sys.stdin:
        text = text.strip() or time.sleep(1)
        filename = "waves/wave-%03d-%s.wav" % (i, text)
        open(filename, "wb").write(synth(text))
        i += 1
