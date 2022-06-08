import re
import argparse
import discord
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description='get user list')
parser.add_argument('token', type=str, help='discord token')
args = parser.parse_args()
token = args.token

print('----------------------------------------')
print('                 Hermes                 ')
print('----------------------------------------')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('----------------------------------------')
    print('Logged in')
    print(f'user name  : {client.user}')
    print(f'user id    : {client.user.id}')
    print(f'discord.py : {discord.__version__}')

    print('----------------------------------------')
    print('Connected guilds')
    for guild in client.guilds:
        print('*', guild.name)

    print('----------------------------------------')
    print('Saving guilds users')
    for guild in client.guilds:
        print('*', guild.name)
        guild_name = re.sub(r'\W+', '', guild.name)

        df = pd.DataFrame()
        df.insert(0, 'id', [])
        df.insert(1, 'name', [])
        for role in sorted(guild.roles, reverse=True, key=lambda role: role.name):
            df.insert(2, str(role), [])

        for member in guild.members:
            member_name = re.sub(r'\W+', '', member.name)
            # print('  *', member.id, '(', member.name, ')')
            member_data = [str(member.id), member_name]
            for role in sorted(guild.roles, key=lambda role: role.name):
                if role in member.roles:
                    member_data.append(str(1))
                else:
                    member_data.append(str(0))
            df.loc[len(df.index)] = member_data
        df.to_csv(f'users/{guild_name}.csv', index_label='index')

    print('----------------------------------------')
    await client.close()

client.run(token)
