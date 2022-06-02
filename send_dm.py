import time
import argparse
import discord
import numpy as np

parser = argparse.ArgumentParser(description='get user list')
parser.add_argument('token', type=str, help='discord token')
parser.add_argument('filename', type=str, help='user filename')
parser.add_argument('message', type=str, help='message filename')
parser.add_argument('--timer', type=int, default=1, help='time to wait (minutes) between messages')
args = parser.parse_args()
token = args.token
filename = args.filename
message = args.message
timer = args.timer

members_id = np.load(filename)
message = open(message, 'r', encoding='utf-8')
message = message.read()

print('----------------------------------------')
print('                 Hermes                 ')
print('----------------------------------------')

client = discord.Client()


@client.event
async def on_ready():
    print('----------------------------------------')
    print('Logged in')
    print(f'user name  : {client.user}')
    print(f'user id    : {client.user.id}')
    print(f'discord.py : {discord.__version__}')

    print('----------------------------------------')

    for member_id in members_id:
        user = await client.fetch_user(member_id)
        result = await user.send(message)
        print(member_id, user, 'ERROR' if result.flags.value else 'OK')
        time.sleep(timer)
    print('----------------------------------------')
    await client.close()


client.run(token)
