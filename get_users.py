import re
import argparse
import discord
import numpy as np

parser = argparse.ArgumentParser(description='get user list')
parser.add_argument('token', type=str, help='discord token')
parser.add_argument('--roles', type=str, nargs='+', default=None, help='names of selected roles')
args = parser.parse_args()
token = args.token
selected_roles = args.roles

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
    print('Guilds roles')
    for guild in client.guilds:
        print('*', guild.name)
        for role in guild.roles:
            print('  *', role.name)
    print('----------------------------------------')
    print('Guilds members')
    members_all = dict()
    for guild in client.guilds:
        print('*', guild.name)
        members = dict()
        for member in guild.members:
            if selected_roles is not None:
                for role in member.roles:
                    if role.name in selected_roles:
                        print('  *', member.id, '(', member.name, ')')
                        members[member.id] = member.name
            else:
                print('  *', member.id, '(', member.name, ')')
                members[member.id] = member.name
        # save
        guild_name = re.sub(r'\W+', '', guild.name)
        np.save(f'users_{guild_name}.npy', np.array(list(members.keys()), dtype=np.int64))
        members_all = {**members_all, **members}
    np.save('users_all.npy', np.array(list(members_all.keys()), dtype=np.int64))
    print('----------------------------------------')
    await client.close()

client.run(token)
