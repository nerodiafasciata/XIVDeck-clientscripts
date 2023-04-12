# XIVDeck-clientscripts
Scripts for interacting with the XIVDeck Dalamud plugin without Elgato software

The goal of this project is to create scripts in python that can be easily mapped to Stream Deck buttons with third party tools.
In order to accomplish this, they will be designed as command line tools.

Currently there's no session handling, so the API key must be passed as an argument. This isn't ideal, but neither is fetching
the API key every time the script is run. So that'll need doing before this can be considered ready to use.

After implementing the POST-based API calls as scripts (which will give a ton of usefulness without too much effort) I'll look into
actually duplicating the functionality of the XIVDeck Elgato plugin.

Tested on Linux with python 3.10, but they should work on any OS.

Working: xivdeck-command.py - used to send a console command via the XIVDeck command API.
