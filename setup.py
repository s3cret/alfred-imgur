# First set up your key things and generate your key.json in folder key/
import sys
sys.path.insert(0, "./modules/api")
from modules.api.util import _store

user = {
    "username": "",
    "client_id": "",
    "client_secret": "",
    "access_token": "",
    "refresh_token": "",
    "account_id": ""
}

_store(user)
