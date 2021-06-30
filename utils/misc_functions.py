import discord

async def test_for_ping(message):
    if message.content == 'ping':
        await message.channel.send('pong')
        
async def greet_member(member):
    print("Greeting possibly")
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!'
    )