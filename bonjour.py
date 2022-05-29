import argparse
import discord

parser = argparse.ArgumentParser(description='get user list')
parser.add_argument('token', type=str, help='discord token')
parser.add_argument('--welcome-id', type=int, default=None, help='welcome channel id')
parser.add_argument('--moderation-id', type=int, default=None, help='moderation channel id')
args = parser.parse_args()
token = args.token
channel_general_id = args.welcome_id
channel_moderation_id = args.moderation_id

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


@client.event
async def on_member_join(member):
    print(f"user {member.display_name} join")
    if channel_general_id is not None:
        channel_general = client.get_channel(channel_general_id)
        await channel_general.send(f"Welcome {member.display_name} !")
    if channel_moderation_id is not None:
        channel_moderation = client.get_channel(channel_moderation_id)
        message = await channel_moderation.send(f"New member {member.display_name}")
        await message.add_reaction('1\uFE0F\u20E3')
        await message.add_reaction('2\uFE0F\u20E3')
        await message.add_reaction('3\uFE0F\u20E3')
        await message.add_reaction('4\uFE0F\u20E3')
        await message.add_reaction('5\uFE0F\u20E3')

client.run(token)
