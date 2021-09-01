import os

import discord
import requests
import time
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


def get_random_pictures():
    client_unsplash = os.getenv('UNSPLASH_CLIENT')
    headers = {'Authorization': 'Client-ID ' + client_unsplash}
    url_unsplash = os.getenv('URL')
    request = requests.get(url=url_unsplash, headers=headers)
    data = request.json()
    return data['urls']['raw']


# Add role "EXCLU" which
#

@bot.command(
    name='monkey',
    help='Just show you beautiful monkeys :3',
    pass_context=True
)
async def monkey(ctx):
    await ctx.send(get_random_pictures())


@bot.command(name='cage')
@commands.has_role('MaitreSinge')
async def cage(ctx, user: discord.Member):
    roles = ['Singe', 'MaitreSinge', 'Lolien', 'Raciste']
    if 'MaitreSinge' in str(user.roles):
        await ctx.send('MOI PEUT PAS METTRE EN CAGE CHEF')
        return
    for role in roles:
        if role in str(user.roles):
            await user.remove_roles(get(user.roles, name=role))
    await user.add_roles(get(user.guild.roles, name='Merde'))
    await ctx.send(str(user.mention) + 'OUH OUH OUH OUH !!!')


@bot.command(name='uncage')
@commands.has_role('MaitreSinge')
async def uncage(ctx, user: discord.Member):
    await user.remove_roles(get(user.roles, name='Merde'))
    await user.add_roles(get(user.guild.roles, name='Singe'))

bot.run(discord_token)