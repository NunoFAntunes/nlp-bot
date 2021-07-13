from discord.ext import tasks,commands
import discord
from random import randrange
import os
# from time import sleep
import re
from asyncio import sleep
import algorithms.time_functions.time_finder as time_finder

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    '''
    Commands
    '''
    
    @commands.command(name='hello')
    async def hello_command(self, ctx):
        await ctx.channel.send("Hello!")
        
    @commands.command(name='roll', aliases=['rolldice'])
    async def roll_dice_command(self, ctx, *args):
        script_dir = os.path.join(os.path.dirname(__file__), os.pardir)
        rel_path = os.path.join(script_dir, "assets", "images", "dice")
        if not args:
            rolled_number = str(randrange(6)+1)
            await ctx.channel.send(file=discord.File(os.path.join(rel_path, "die_face_%s.png" % rolled_number)))
        else:
            await ctx.channel.send(file=discord.File(os.path.join(rel_path, "roll.gif")))
            if len(args) > 1:
                await ctx.channel.send("Too many arguments passed. Only the first was taken into consideration")
            try:
                dice_size = int(args[0])
                await ctx.channel.send(str(randrange(dice_size)+1))
            except:
                await ctx.channel.send("Is that really a number?")
                
    async def countdown_recursive(self, ctx, seconds, timer_type):
        if(seconds == 0):
            await ctx.message.reply("Your timer is up!")
        else:
            seconds = seconds-1
            print(seconds)
            if(timer_type == 0):
                if(seconds%15==0 and seconds != 0):
                    await ctx.channel.send('%s seconds remaining!' % str(seconds))
            elif(timer_type == 1):
                if(seconds%60==0):
                    await ctx.channel.send('%s minutes remaining!' % str(seconds/60))
                elif(seconds<60 and seconds%15==0 and seconds != 0):
                    await ctx.channel.send('%s seconds remaining!' % str(seconds))
            else:
                if(seconds%3600==0):
                    await ctx.channel.send('%s hours remaining!' % str(seconds/3600))
                elif(seconds<3600 and seconds%60==0):
                    await ctx.channel.send('%s minutes remaining!' % str(seconds/60))
                elif(seconds<60 and seconds%15==0 and seconds != 0):
                    await ctx.channel.send('%s seconds remaining!' % str(seconds))
            await sleep(1)
            return await self.countdown_recursive(ctx, seconds, timer_type)
        
     
    @commands.command(name='timer')
    async def timer_command(self, ctx, *text):
        sentence = ' '.join(word for word in text)
        seconds, timer_type = time_finder.find_timer_time(sentence)
        await ctx.message.add_reaction("🕒")
        await ctx.channel.send('Starting a %s Seconds Timer.' % str(seconds))
        await self.countdown_recursive(ctx, seconds, timer_type)
        
    @commands.command(name='chat')
    async def chat(self, ctx, *text):
        await ctx.channel.send('Hello my friend!')
        def check(m):
            return m.content == 'How are you' and m.channel == ctx.channel

        msg = await self.bot.wait_for('message', check=check)
        await ctx.channel.send('Doing good {.author}! How about you?'.format(msg))
                    
def setup(bot):
    bot.add_cog(MiscCommands(bot))