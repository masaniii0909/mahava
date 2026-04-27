# mahava
My Attempt at Home assistant Voice Assistant

highschool comp sci student's attempt at a hackable home assistant.

# features

### super ez wakeword setting!
- in the 15th line, you are easily able to change the wakeword to anything you want, granted the speech recognizer gets it right.
- NO TRAINING MODELS!! Vosk is really awesome and i just use it for your wakeword to be recognized.
### custom voices!
- through the magic that is tts_with_rvc, you are easily able to use almost any voice you want
- slower with bigger responses however
### make ur own features + commands
- all commands are the elif statements that listen for the wakeword and whatever prompt is in there
- this does come with some caveats, however.
### premade commands 
- some media control commands are already made! however they are for spotify.
- timer
- this can help you get started on adding more commands and features!
### future features
- home assistant like features such as telling stories, alarms, reminders, etc. 
- asking for weather
- have version a as a server
- computer vision??
- chatbot??


# reqs
requires the following:

- linux x86 (tested on arch only)
- python 3.12
- word2number
- vosk
- ollama
- tts_with_rvc 
- sounddevice

# disclaimer
has been tested on three pcs, one with a ryzen 7 5800xt and nvidia 3060. it is very fast on that machine.
but on another machine with an intel i7 8th gen and 1660ti, it is noticeably slower, especially because of the tts with rvc. i'll release a server version where something like an rpi could be a mic+speaker and sends the vosk speech recognition to a pc. 
