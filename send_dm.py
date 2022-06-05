import time
import random
import argparse
import discord
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description='get user list')
parser.add_argument('token', type=str, help='discord token')
parser.add_argument('filename', type=str, help='user filename')
parser.add_argument('message', type=str, help='message filename')
parser.add_argument('--timer', type=int, default=1, help='time to wait (seconds) between messages')
parser.add_argument('--timer-random', type=int, default=5, help='random time to add to timer (max value)')
parser.add_argument('--anti-spam-counter', type=int, default=10,
                    help='message to send to trigger anti-spam-timer')
parser.add_argument('--anti-spam-timer', type=int, default=45,
                    help='time to wait (seconds) between anti-spam-counter messages')
parser.add_argument('--anti-spam-timer-random', type=int, default=60,
                    help='random time to add to anti-spam-timer (max value)')

args = parser.parse_args()
token = args.token
filename = args.filename
message = args.message
timer = args.timer
timer_random = args.timer_random
anti_spam_counter = args.anti_spam_counter
anti_spam_timer = args.anti_spam_timer
anti_spam_timer_random = args.anti_spam_timer_random

members = pd.read_csv(filename, sep=',')

message = open(message, 'r', encoding='utf-8')
message = message.read()

print('----------------------------------------')
print('                 Hermes                 ')
print('----------------------------------------')

client = discord.Client()
hermes_run = False


@client.event
async def on_ready():
    print('----------------------------------------')
    print('Logged in')
    print(f'user name  : {client.user}')
    print(f'user id    : {client.user.id}')
    print(f'discord.py : {discord.__version__}')

    print('----------------------------------------')
    ret_hermes = await hermes()
    print("hermes() :", ret_hermes)
    print('----------------------------------------')
    if ret_hermes == 0:
        await client.close()


async def hermes():
    global hermes_run
    if hermes_run:
        return 42
    else:
        hermes_run = True

    i = 0
    for _, member in members.iterrows():
        time.sleep(1.0)
        print(member['id'], end=" ")
        user = await client.fetch_user(member['id'])
        print(user, end=" ")
        try:
            result = await user.send(message)
            print('ERROR' if result.flags.value else 'OK')
        except Exception as e:
            print('ERROR')
        # anti spam A
        time.sleep(timer)
        time.sleep(random.random()*timer_random)
        # anti spam B
        if i > 0 and i % anti_spam_counter == 0:
            pause = float(anti_spam_timer) + random.random()*float(anti_spam_timer_random)
            print("anti spam pause:", pause)
            time.sleep(pause)
        i += 1

    return 0


client.run(token)
