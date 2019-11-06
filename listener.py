import json, sys, itertools, time
from json import JSONDecodeError
from websocket import create_connection
import requests
import pyttsx3
import ssl
import os

print("Thanks for Running Halligan Listener")

engine = pyttsx3.init()
engine.setProperty('rate', 180)

ws = create_connection("wss://www.halliganhelper.com/ws/ta?subscribe-broadcast", sslopt={"cert_reqs": ssl.CERT_NONE})

# environment variables for accessing login email and password
email_env_var = "HALLIGAN_HELPER_EMAIL"
pass_env_var  = "HALLIGAN_HELPER_PASS"

# seconds after ping fail
retryInterval = 5

# fill this in before running
loginEmail = os.environ.get(email_env_var)
loginPassword = os.environ.get(pass_env_var)

assert (loginEmail is not None), 'login email not set'
assert (loginPassword is not None), 'login password not set'

r = requests.post('https://www.halliganhelper.com/api/v3/user/login/',
                  data = {'email': loginEmail, 'password': loginPassword}, verify = False)

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
    except OSError:
        time.sleep(retryInterval)
        # usually due to network being temporarily down
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
