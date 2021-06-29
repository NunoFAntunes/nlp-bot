from utils import misc_functions


import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        misc_functions.test_for_ping(message)

client = MyClient()
client.run('ODU5MjQ5NDc1NDMyMjE4NjM0.YNp8bw.spiM7SKAPD7Bd3SJl9meVl0tadg')