#!/bin/bash

# See: http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
DIR="/home/atamon/code/xbmcplay.py"

#echo "The script you are running has basename `basename $0`, dirname `dirname $0`"

# Proxy to the python executable
python "$DIR/client.py" "$@"