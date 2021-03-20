import json
import sys, os
from modules.api.util import auth
sys.path.insert(0, "./modules/api")

from util import *


try:
    last_info = sys.argv[1]
except IndexError:
    print("Please provide last image info file path.")
    exit(1)

with open(os.path.join("uploaded", last_info)) as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        print("JSON file decoder error.")
        exit(1)

i = auth()
res1 = i.delete_image(data["id"])
res2 = i.album_remove_images(data["album"], data["id"])

if res1 and res2:
    print("Successfully removed the last uploaded image.")
    exit(0)
else:
    print("Failed with the external reasons.")
    exit(1)
