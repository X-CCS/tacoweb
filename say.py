#!/home/pi/say/say/bin/python3

import subprocess
import sys
import time
import os
import os.path
import urllib.parse
import urllib.request
import datetime

def dateparse_generator():
    import dateparser
    settings = dateparser.conf.Settings()
    settings.PREFER_DATES_FROM = 'future'
    return lambda date: dateparser.parse(date, settings=settings)
dateparse = dateparse_generator()

URL = "http://192.168.0.198:9997?"

DIR = "what"

def synth(z):
    r = urllib.request.urlopen(URL + urllib.parse.quote(z))
    assert r.headers['content-type'] == "audio/x-wav"
    return r.read()

def play(zz):
    CMD = ["/usr/bin/aplay", "-Ddefault", "-q", "-"]
    subprocess.run(CMD, input=zz)

if __name__ == "__main__":
    def reload():
        now = datetime.datetime.now()
        sayqueue = []
        for file in os.listdir(DIR):
            print("checking", file)
            try:
                if file[0] == ".":
                    continue
                path = os.path.join(DIR, file)
                fobj = open(path, "r")
                date = fobj.readline().strip()
                dateparsed = dateparse(date)
                retext = dateparsed.strftime("%c")
                print(date, retext)
                if dateparsed < now:
                    line = [text.strip() for text in fobj]
                    sayqueue.append(line)
                    os.rename(path, os.path.join("what.done", file))
                    log = open("say.log", "a")
                    log.write(date + "\n")
                    log.write("".join(text + "\n" for text in line))
                    log.close()
                elif retext != date:
                    # write in what date we think
                    text = fobj.read()
                    fobj = open(path, "w")
                    fobj.write(retext + "\n")
                    fobj.write(text)
            except Exception as e:
                import traceback
                traceback.print_exc()
        for file in sayqueue:
            wavs = []
            for li in file:
                if li == "":
                    wavs += [None]
                else:
                    wavs += [synth(li)]
            for wav in wavs:
                if wav:
                    play(wav)
                time.sleep(0.2)
            if len(sayqueue) > 0:
                time.sleep(1)
        time.sleep(1)
    while True:
        reload()
