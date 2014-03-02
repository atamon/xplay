import requests
import json


def reboot(options):
    payload = {
        'method': 'System.Reboot'
    }

    payload.update(options['payloadDefaults'])

    r = requests.post(options['url'], data=json.dumps(payload))
    data = r.json()

    if ('error' in data):
        print('Failed to reboot XBMC system')
    else:
        print('Rebooting XBMC system')
