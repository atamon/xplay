import os
import sys
import json
from string import join

import player
import system
from matcher import Matcher


def matchCommand(string, options):
    # Handle keywords (play, pause, stop, jumpto)
    keywordMap = {
        'play': player.play,
        'pause': player.pause,
        'stop': player.stop,
        'jumpto': player.jumpTo,
        'reboot': system.reboot,
    }

    command = keywordMap.get(string)

    # Catch keywords
    if (command):
        command(options=options)
    else:
        # Default to finding files through the Matcher class
        m = Matcher(string, options)
        m.matchVideo()


# Set up configuration from file
mydir = os.path.dirname(os.path.realpath(__file__))
optionsString = open(mydir + '/config.json')
options = json.load(optionsString)

# Parse command line arguments

argument = join(sys.argv[1::])

matchCommand(argument, options)
