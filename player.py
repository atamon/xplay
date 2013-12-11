import requests
import json


def playFile(file, options):
    payload = {
        'method': 'Player.Open',
        'params': {
            'item': {
                'file': file['file']
            }
        }
    }

    payload.update(options['payloadDefaults'])

    r = requests.post(options['url'], data=json.dumps(payload))
    data = r.json()

    if ('error' in data or not 'result' in data):
        raise Exception(data)
    else:
        print('Playing file {0}'.format(file['label']))


def play():
    print('MockPlay')


def pause():
    print('MockPause')


def stop():
    print('MockStop')


"""Real playPause request to XBMC"""
def playPause():
    print('MockPlayPause')


def jumpTo(hour, minute, second):
    print('{0}:{1}:{2}'.format(hour, minute, second))
