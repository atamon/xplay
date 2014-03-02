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


def play(options):
    payload = {
        'method': 'Player.playPause',
        'params': {
            'playerid': 1,
            'play': True
        }
    }

    payload.update(options['payloadDefaults'])

    r = requests.post(options['url'], data=json.dumps(payload))
    data = r.json()

    if ('error' in data or not 'result' in data):
        raise Exception(data)
    else:
        print('Playback resumed')


def pause(options):
    payload = {
        'method': 'Player.playPause',
        'params': {
            'playerid': 1,
            'play': False
        }
    }

    payload.update(options['payloadDefaults'])

    r = requests.post(options['url'], data=json.dumps(payload))
    data = r.json()

    if ('error' in data or not 'result' in data):
        raise Exception(data)
    else:
        print('Playback paused')


def stop(options):
    payload = {
        'method': 'Player.Stop',
        'params': {
            'playerid': 1
        }
    }

    payload.update(options['payloadDefaults'])

    r = requests.post(options['url'], data=json.dumps(payload))
    data = r.json()

    if ('error' in data):
        print('Failed to stop playback, maybe there\'s nothing\'s playing? :)')
    else:
        print('Playback stopped')


def playPause(options):
    """Real playPause request to XBMC"""
    print('MockPlayPause')


def jumpTo(hour, minute, second):
    print('MockJumping to {0}:{1}:{2}'.format(hour, minute, second))