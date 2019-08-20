#!/usr/bin/env python3

import discord
import details
import image


client = discord.Client()
@client.event
async def on_message(msg):
    if msg.author.id != client.user.id:
        print_to_term(msg)
        await process_command(msg)

    return



@client.event
async def on_ready():
    print('Logged in as {}'.format(client.user))


def print_to_term(msg):
    print('{}({}): '.format(msg.author.name, msg.author.id), end='')
    print(str(msg.content), flush=True)

async def _help(msg):
    top = 'Availible commands'

    commands = '''
help: Bring up this message
album: Upload images to create an album
'''

    em = discord.Embed(description=commands)
    await msg.channel.send(top, embed=em)


async def create_album(msg):
    channel = msg.channel

    await channel.send('Please send the required images (1 per message) and type {}done when all photos have been sent'.format(details.PREFIX))

    def check(m):
        return m.channel == msg.channel and m.author == msg.author

    response = await client.wait_for('message', check=check)

    urls = []
    ids = []

    while(response.content != '!done'):
        for x in response.attachments:
            urls.append(x.url)
            try:
                image_id = image.upload_image(x.url)
            except Exception as e:
                print('Ran into and error uploading image:\n{}'.format(e))
                await channel.send('Sorry, the bot is currently being rate limited,'
                       + ' or ran into an error. Please try again later.\n')
                return
            ids.append(image_id)
            await response.add_reaction('✅')
        response = await client.wait_for('message', check=check)

    if len(ids) < 1:
        await channel.send('No images sent. Aborting upload, please try again later.')
        return


    album_id = image.create_album(ids)

    url = 'https://imgur.com/a/{}'.format(album_id)
    await channel.send('Here is your album url: {}'.format(url))





async def process_command(msg):
    if not msg.content.startswith(details.PREFIX):
        return

    if len(details.BOT_CHANNELS) > 0:
        if msg.channel.id not in details.BOT_CHANNELS and not(
                type(msg.channel) == discord.DMChannel):
            return

    if not details.PM and type(msg.channel) == discord.DMChannel:
        return

    tokens = msg.content.split(' ')
    commands = {
            'help': _help,
            'album': create_album,
            }
    command = commands.get(tokens[0][1:])

    if command is not None:
        await command(msg)


client.run(details.token)
