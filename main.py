from utils import misc_functions

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        await misc_functions.test_for_ping(message)
        
    async def on_member_join(member):
        print("In function")
        await misc_functions.greet_member(member)

client = MyClient()
client.run(TOKEN)