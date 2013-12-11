import sys
import json

import player
from matcher import Matcher


def matchCommand(string):
    # Handle keywords (play, pause, stop, jumpto)
    keywordMap = {
        'play': player.play,
        'pause': player.pause,
        'stop': player.stop,
        'jumpto': player.jumpTo
    }

    command = keywordMap.get(string)

    # Catch keywords
    if (command):
        print(command)
        command()
    else:
        # Default to finding files through the Matcher class
        m = Matcher(string, options)
        m.matchVideo()


# Set up configuration from file
optionsString = open('config.json')
options = json.load(optionsString)

matchCommand(sys.argv[1])
