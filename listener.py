import json, sys, itertools
from json import JSONDecodeError
from websocket import create_connection
import requests
import pyttsx3

# This is a file where I store my login info
import credentials

print("Thanks for Running Halligan Listener")

engine = pyttsx3.init()
engine.setProperty('rate', 180)

ws = create_connection("wss://www.halliganhelper.com/ws/ta?subscribe-broadcast")

# replace credentials.login and credentials.password with your own
r = requests.post('https://www.halliganhelper.com/api/v3/user/login/',
                  data = {'email': credentials.login, 'password': credentials.password})

def getInfo (res):
    id = res['data']['id']
    info = requests.get('https://www.halliganhelper.com/api/v3/school/courses/16/requests/' + str(id), cookies = r.cookies, verify=False)
    req = json.loads(info.text)

    out = ("New request: {}, at {}, by {}".format(req['question'], req['where_located'], req['requestor']['first_name']))
    print("[NEW] {}".format(out))
    say (out)

def say (out):
    engine.say(out)
    engine.runAndWait()

print("Standing by ...")
while (True):
    ping = {}
    try:
        ping = json.loads(ws.recv())
    except JSONDecodeError:
        pass
    else:
        if (ping['type'] == 'request_created'):
            getInfo(ping)
        elif (ping['type'] == 'request_updated'):
            # checked out or edited request
            pass
        elif (ping['type'] == 'request_removed'):
            # resolved or canceled
            pass

ws.close()
