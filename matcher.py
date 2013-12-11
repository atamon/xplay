import re
import json
import requests

import player


class Matcher(object):
    def __init__(self, string, options={}):
        self.string = string
        self.options = options

    def presentMatches(self, matches):
        nMatches = len(matches)
        for index, file in enumerate(matches):
            message = '({0}/{1}) Play "{2}" ? [Y/n]: '.format(index + 1,
                                                              nMatches,
                                                              file['label'])
            play = raw_input(message)

            if not (play):
                play = 'Y'

            if (play == 'Y'):
                return file

    def fetchDirectory(self, directory):
        payload = {
            'method': 'Files.GetDirectory',
            'params': {
                'directory': directory
            }
        }

        payload.update(self.options['payloadDefaults'])

        url = self.options['url']

        r2 = requests.post(url, data=json.dumps(payload))

        data = r2.json()

        if ('error' in data or not 'result' in data):
            raise Exception(data)

        return data['result']['files']

    def parseContents(self, contents):
        tester = re.compile(self.string, re.IGNORECASE)
        directories = []
        matches = []

        for file in contents:
            if (file['filetype'] == 'directory'):
                directories.append(file)
            elif(tester.match(file['label'])):
                matches.append(file)

        return {
            'files': matches,
            'directories': directories
        }

    def matchVideo(self):
        print('Matching "{0}"'.format(self.string))

        contents = self.fetchDirectory(self.options['rootDirectory'])
        pContents = self.parseContents(contents)
        matches = pContents['files']

        selectedFile = self.presentMatches(matches)

        if not (selectedFile):
            for directory in pContents['directories']:
                dirContents = self.fetchDirectory(directory['file'])
                if (dirContents):
                    pDirContents = self.parseContents(dirContents)
                    selectedFile = self.presentMatches(pDirContents['files'])

                    if (selectedFile):
                        player.playFile(selectedFile, self.options)
                        break
        else:
            player.playFile(selectedFile, self.options)
