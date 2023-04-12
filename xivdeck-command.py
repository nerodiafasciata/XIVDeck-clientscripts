#!/usr/bin/python3
#===============================================#
# xivdeck-command
# Version 0.01
# by nerodia
#===============================================#

# need requests for html and args
import requests
import argparse

parser = argparse.ArgumentParser(
    prog='xivdeck-command',
    description='Send a console command to XIVDeck',
    epilog = 'Example: python3 xivdeck-command.py -p 38500 9O6RrAGhMWrk9qipOPQ7dGmIDp5KUOe/ /gaction "Mount Roulette"')
parser.add_argument('-p', '--port', default='37984')
parser.add_argument('api key', help='API key, obtainable via curl http://127.0.0.1:37984/diagnostics')
parser.add_argument('command', help='Command to send.')

args = parser.parse_args()

