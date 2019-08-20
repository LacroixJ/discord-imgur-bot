# Discord Imgur Bot
- - -


## Setup

run the following commands
`sudo pip3 install discord`
`sudo pip3 install imgurpython`

##### Imgur Setup
Register your bot at <https://api.imgur.com/oauth2/addclient>

Note down the **access key** and **secret**, and insert these into `details.py`


`./authenticate_imgur.py` or `python3 authenticate_imgur.py`

Follow the intructions given, and you will recieve access and refresh tokens.
Insert both of these into their respective spots in `details.py`

##### bot setup
Please follow the instructions at <https://discordapp.com/developers/applications/> to setup your bot and recieve an access token. Paste this token into `details.py`

## Configuration
There are a few options in `details.py` that may be configured.

You may choose the prefix for the bot with the `PREFIX` variable. The default prefix is `!`

You can choose which channels the bot can be used on with the `BOT_CHANNELS` variable. Just insert the channel ids.

Finally, you may decide if the bot can be interacted with via private message with the `PM` variable. Default is `True`.

## Usage

Run the bot with `./bot.py` or `python3 bot.py`

You can type `!help` to see the commands, and `!album` to start uploading pictures.

If you would like to run the bot to verify it works without actually making any requests.
Replace `import image.py` with `import mock_image.py` in the first lines of `bot.py`
