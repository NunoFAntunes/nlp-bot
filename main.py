from utils import misc_functions

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['-', 'lol ', '!?']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.Administration',
                      'cogs.CommandEvents',
                      'cogs.HelpCommands',
                      'cogs.MiscCommands',
                      'cogs.GoogleCommands']

bot = commands.Bot(command_prefix=get_prefix, description='SmortBot')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
        
@bot.event
async def on_ready():
#    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    # await bot.change_presence(activity=discord.Game(name='Being Smort', type=1))
    print(f'Successfully logged in and booted...!')


#@bot.event
#async def on_ready(self):
#    print('Logged on as {0}!'.format(self.user))
#
#    async def on_message(self, message):
#        print('Message from {0.author}: {0.content}'.format(message))
#        
#        await misc_functions.test_for_ping(message)
#        
#    async def on_member_join(member):
#        print("In function")
#        await misc_functions.greet_member(member)


bot.run(TOKEN, reconnect=True)