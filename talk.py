#!/home/pi/say/say/bin/python3

import subprocess, sys, time, os.path
import urllib.request, urllib.parse

URL = # http://SERVER_URL_HERE:9997/?

class wait:
    def __init__(self):
        self.wait = []
        self.ix = 0

    def add(self, when, f):
        heapq.heappush(self.wait, (when, self.ix, f))
        self.ix += 1

    def wait(self, timeout):
        if len(self.wait) == 0:
            time.sleep(timeout)
        else:
            when, _, fn = self.wait[0]
            now = time.time()
            until = now + timeout
            if when > until:
                time.sleep(timeout)
            else:
                if when > now:
                    time.sleep(when - now)
                heapq.heappop(self.wait)
                fn()

class waiter:
    def __init__(self, fn):
        self.filename = fn

    def gettime(self):
        return parse(open(self.filename, "rb").readline().strip())

    def addto(self, waitobj, f):
        t = self.gettime()
        waitobj.add(t, f)

    def gettext(self):
        fobj = open(self.filename, "rb")
        fobj.readline()
        return [l.strip() for l in fobj]

class watcher:
    def __init__(self, fn):
        self.dir = fn
        self.files = {}
        self.wobj = wait()
        self.synther = synth

    def loop(self):
        for file in os.listdir(self.dir):
            if file in self.files:
                continue
            else:
                pass

def synth(z):
    r = urllib.request.urlopen(URL + urllib.parse.quote(z))
    assert r.headers['content-type'] == "audio/x-wav"
    zz = r.read()
    CMD = ["/usr/bin/aplay", "-Ddefault", "-q", "-"]
    subprocess.run(CMD, input=zz)

if __name__ == "__main__":
    for text in sys.stdin:
        text = text.strip() or time.sleep(1)
        if text: zz = synth(text)
