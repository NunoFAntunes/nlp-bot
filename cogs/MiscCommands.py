from discord.ext import commands
import discord
from random import randrange
import os

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
        rel_path = "assets\\images\\dice"
        if not args:
            rolled_number = str(randrange(6)+1)
            await ctx.channel.send(file=discord.File(os.path.join(script_dir, rel_path, "die_face_%s.png" % rolled_number)))
        else:
            await ctx.channel.send(file=discord.File(os.path.join(script_dir, rel_path, "roll.gif")))
            if len(args) > 1:
                await ctx.channel.send("Too many arguments passed. Only the first was taken into consideration")
            try:
                dice_size = int(args[0])
                await ctx.channel.send(str(randrange(dice_size)+1))
            except:
                await ctx.channel.send("Is that really a number?")
    
     
     
       
def setup(bot):
    bot.add_cog(MiscCommands(bot))