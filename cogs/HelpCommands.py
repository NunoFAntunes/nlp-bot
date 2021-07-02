from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(name='h', invoke_without_command=True) 
    async def helpcommand(self, ctx):
        await ctx.channel.send("Global help command goes here. :)")
       
    @helpcommand.command(name='ping') 
    async def ping_help(self, ctx):
        await ctx.channel.send("Checks if the man is working or being lazy.")
        
def setup(bot):
    bot.add_cog(HelpCommands(bot))