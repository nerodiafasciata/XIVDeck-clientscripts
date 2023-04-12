#!/usr/bin/python3
#===============================================#
# xivdeck-command
# Version 0.01
# by nerodia
#===============================================#

# need requests for html, argparse for usability, json for dumps
import requests
import argparse
import json

# make it not suck to use
parser = argparse.ArgumentParser(
    prog='xivdeck-command',
    description='Send a console command to XIVDeck',
    epilog='Example: python xivdeck-command.py -p 38500 -a 9O6RrAGhMWrk9qipOPQ7dGmIDp5KUOe/ \'/gaction "Mount Roulette"\'')

# arguments
# todo: figure out a way to cache the apikey without overcomplicating things
parser.add_argument('-p', '--port', default='37984',
                    help='Only necessary if changed from the default 37984')
parser.add_argument('-a', '--apikey',
                    help='API key, obtainable via curl http://127.0.0.1:37984/diagnostics')
parser.add_argument('command',
                    help='Command to send. Surround with single quotes to avoid issues')


args = parser.parse_args()

# make this shitcode easy to read
addr = 'http://127.0.0.1:' + args.port + '/command'
command = args.command
apikey = args.apikey

# send the command, handle exceptions gracefully, inform user about likely cause of errors
try:
    req = requests.post(addr,
                        json.dumps({'command': command}),
                        headers={'Authorization': 'Bearer ' + apikey})
    req.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
    print('#### check that you are using the correct API key ####')
except requests.exceptions.RequestException as e:
    print(e)
    print('#### check that XIVDeck is running and that you are using the correct port ####')
