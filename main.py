import logging
import os
import platform
import sys

import discord
from discord.ext import commands

from config import secrets, settings

bot = commands.Bot(
    command_prefix = '!',
    intents = discord.Intents.all(),
    application_id = settings.APPLICATION_ID,
    log_handler = logging.basicConfig(stream=sys.stdout, level=logging.WARNING)
)
bot.remove_command('help')
bot.synced = False

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('---------------------------------------------------')
    print(f'Logged in as {bot.user.name} | {bot.user.id}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')
    print('---------------------------------------------------')

if __name__ == '__main__':
    for file in os.listdir('cogs/'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

bot.run(secrets.BOT_TOKEN)
