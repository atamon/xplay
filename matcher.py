import re
import json
from sys import stdout
from requests_futures.sessions import FuturesSession
from functools import partial


def match(source, subject):
    for part in source.split(' '):
        test = re.compile('.*' + part + '.*', re.IGNORECASE)

        if not (test.match(subject)):
            return False

    return True


class Matcher(object):
    def __init__(self, string, options={}):
        self.string = string
        self.options = options

        self.match = partial(match, source=string)

        self.session = FuturesSession(max_workers=10)

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

        return self.session.post(
            url,
            data=json.dumps(payload),
            background_callback=self.handleDirectoryResult)

    def handleDirectoryResult(self, session, response):
        data = response.json()

        if ('error' in data or not 'result' in data):
            raise Exception(data)

        files = data['result']['files']
        contents = self.parseContents(files)

        response.futures = []
        for d in contents['directories']:
            future = self.fetchDirectory(d['file'])
            response.futures.append(future)

        response.matches = contents['files']
        self.log(".")

    def parseContents(self, contents):
        directories = []
        matches = []

        if contents is not None:
            for file in contents:
                if (file['filetype'] == 'directory'):
                    directories.append(file)
                elif(self.match(subject=file['label'])):
                    matches.append(file)

        return {
            'files': matches,
            'directories': directories
        }

    def gatherMatches(self, future):
        matches = []
        response = future.result()
        for sf in response.futures:
            matches.extend(self.gatherMatches(sf))

        matches.extend(response.matches)
        return matches

    def log(self, msg, linebreak=False):
        stdout.write(msg)
        if linebreak:
            stdout.write('\n')
        stdout.flush()

    def matchVideo(self):
        self.log('Matching "{0}" '.format(self.string))

        future = self.fetchDirectory(self.options['rootDirectory'])
        matches = self.gatherMatches(future)
        self.log("", True)
        self.presentMatches(matches)