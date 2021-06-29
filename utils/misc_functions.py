async def test_for_ping(message):
    if message.content == 'ping':
        await message.channel.send('pong')