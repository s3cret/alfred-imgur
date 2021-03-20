import sys, os
import pasteboard
from imgurpython.helpers.error import ImgurClientError

sys.path.insert(0, "./modules/api")
import album_id

from util import *
image_path = ""
description = ""

try:
    image_path = sys.argv[1]
except IndexError:
    print("Please start by main.sh which will pass in the file path.")
    exit(1)

if "URL" in image_path:
    image_path = pasteboard.Pasteboard().get_contents()
    if "http" not in image_path:
        # exit code 2: Neither file path or url is not provided.
        print("No Image URL found in clipboard.")
        exit(2)

try:
    description = sys.argv[2]
except IndexError:
    # it's ok not to provide with description
    pass

config = {
    "album": album_id.alfred,
    # "album": album_id.hello_imgur,
    "description": description,
}

i = auth()

# 1
# upload image to specific album and store the info
response = dict()

if isfile(image_path):
    response = i.upload_from_path(image_path, config=config, anon=False)
else:
    try:
        response = i.upload_from_url(image_path,config=config, anon=False)
    except ImgurClientError as err:
        print("ImgurClientError({}):\n".format(err.status_code), err.error_message, end=".", sep="")
        exit(1)
    
save(response, config["album"])

