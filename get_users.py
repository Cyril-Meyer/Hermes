import re
import argparse
import discord
import numpy as np

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
        f = open(f'users/{guild_name}.csv', 'w', encoding='utf-8')
        f.write('id,')
        f.write('name')
        for role in guild.roles:
            role_name = re.sub(r'\W+', '', role.name)
            f.write(f',{role_name}')
            print('  *', role.name)
        f.write('\n')

        for member in guild.members:
            member_name = re.sub(r'\W+', '', member.name)
            print('  *', member.id, '(', member.name, ')')
            f.write(f'{member.id},')
            f.write(f'{member_name}')
            for role in guild.roles:
                if role in member.roles:
                    f.write(f',1')
                else:
                    f.write(f',0')
            f.write('\n')
        f.close()
    print('----------------------------------------')
    await client.close()

client.run(token)
