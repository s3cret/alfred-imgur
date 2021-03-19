import datetime
import json
import requests
import album_id

from imgurpython import ImgurClient
from os.path import dirname as dir
from os.path import join
from os.path import isfile
from modules.api.keywords import *


root_dir = dir(dir(dir(__file__)))
_key_path = join(root_dir, "key/key.json")


def _store(user: dict):

    with open(_key_path, "w") as f:
        f.write(json.dumps(user))


def get_key() -> dict:

    data = dict()

    with open(_key_path, "r") as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError as e:
            pass

    return data


def save(info: dict):

    current_time = datetime.datetime.now().strftime("%G-%u-%V at %H:%M:%S")
    filename = "uploaded/" + current_time + " info.json"

    with open(filename, "w+") as f:
        json.dump(info, f)

    # print(filename, "saved!")
    # print("Imgur image posted at:\n{0}".format(info['link']))
    print(info['link'])


def auth() -> ImgurClient:

    key = get_key()
    client = ImgurClient(key[client_id], key[client_secret],
                         key[access_token], key[refresh_token])

    return client


def _update(new: dict):
    # update access_token and refresh_token

    with open(_key_path, "r") as f:
        old = get_key()
        if access_token in new.keys():
            old[access_token] = new[access_token]
        if refresh_token in new.keys():
            old[refresh_token] = new[refresh_token]

    with open(_key_path, "w") as f:
        json.dump(old, f)

    print("Updated!")


def _regenerate_access_token():

    key = get_key()

    url = "https://api.imgur.com/oauth2/token"

    payload = {
        'refresh_token': key[refresh_token],
        'client_id': key[client_id],
        'client_secret': key[client_secret],
        'grant_type': 'refresh_token'
    }

    files = [

    ]

    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    raw_data = response.text
    data = json.loads(raw_data)
    _update(data)

