This repository backs up a little web server that you can run
from the tacotron2 directory (https://github.com/NVIDIA/tacotron2)
and a little client that makes requests and plays them to the
speaker.

IMPORTANT NOTE: tacotron2 will cut off if the input text is too
  long, and it doesn't like it when there is no punctuation on
  the end of a short line. so, break long text on multiple lines.

```
server/tacoweb: the web server.

server/phonetics: a list of phonetic replacements
                  for words that are pronounced wrong.
                  uses tacotron's ARPABET capability.

client/say.py: play scheduled text.
  connects to tacoweb at specific times and requests speech synthesis, then plays it over the speaker.
  to schedule a speech, put files in client/what
  the format is:
    
    in 20 minutes
    It is twenty minutes since you put this file here.

  the first line is parsed by dateparser.parse and the file is
  overwritten with the parsed date so you can check that the
  date is good. for example, the above file would be written
  back out as

    Tue Jun  2 11:57:43 2020
    It is twenty minutes since you put this file here.

  when the date comes around, then it connects to tacoweb and gets
  wavs for each line of the input. there is a pause between lines.

  I was too lazy to deal with time zones so these are local
  times.

client/talk.py: speech synthesizer. text comes from stdin.
  for each line of the input, it connects to tacoweb and gets a wav, and then plays the wav with aplay.
  there is a pause between lines.
  just like say.py except it happens right away.

client/wave.py: like talk.py, but it saves the wavs instead.
  for each line of the input, it connects to tacoweb and gets a wav, and then saves it in wavs/

client/covidcase.py
  read out the number of confirmed infections and deaths
  in Montreal, using Radio-Canada data from the url
    https://kustom.radio-canada.ca/coronavirus/canada_quebec_montreal
```
