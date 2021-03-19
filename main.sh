#!/bin/bash

export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
CUR_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

# $1 (Optional) is -s --screenshot or -c --clipboard
# $2 (Optional) is the pic description

# nothing from arg
if [ $# -eq 0 ]; then
	set -- "-c"
fi

# it's description
if [ "$1" != "-c" ] && [ "$1" != "-s" ] ; then
	set -- "$1" "$1"
	set -- "-c" "$2"
fi

# it's from clipboard
if [ "$1" == "-c" ]; then
	DIR="/tmp/alfred-imgur/clipboard/"
	mkdir -p $DIR
	DATE=`date +"%Y-%m-%d_%H_%M_%S"`
	FILENAME="$DIR$DATE.png"

# from screenshot
elif [ "$1" == "-s" ]; then

	DIR=$(defaults read com.apple.screencapture location 2>/dev/null)
	if [ ! -d "$DIR" ]; then
		USER=$(whoami)
		DIR="/Users/$USER/Desktop/"
	fi
	FILE=$(ls -t "$DIR" | head -n 1)
	FILENAME=$DIR$FILE

fi

# paste to folder /tmp/alfred-imgur/clipboard/
/usr/local/bin/pngpaste $FILENAME 2>/dev/null

if [ $? -ne 0 ] ; then
	FILENAME="Copied URL"
fi

echo $FILENAME=$2
