from googleapi import google
from googleapi import google, images

import discord
from discord.ext import commands
from algorithms.google_functions import youtube_call

class GoogleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    '''
    Commands
    '''
    
    @commands.command(name='google')
    async def google_search_command(self, ctx, input_query):
        search_results = google.search(input_query)
        await ctx.channel.send("This is going to be the result of the search!")
        
    @commands.command(name='calculate')
    async def calculate_command(self, ctx, input_query):
        search_results = google.search(input_query)
        await ctx.channel.send(search_results)
        
    @commands.command(name='img')
    async def img_command(self, ctx, input_query):
        options = images.ImageOptions()
        #options.image_type = images.ImageType.CLIPART
        #options.larger_than = images.LargerThan.MP_4
        #options.color = "green"
        results = google.search_images(input_query, options)
        await ctx.channel.send(results)
     
    @commands.command(name='convert')
    async def convert_command(self, ctx, input_query):
        euros = google.convert_currency(5.0, "USD", "EUR")
        await ctx.channel.send("5.0 USD = {0} EUR".format(euros))
        
    @commands.command(name='youtube', aliases=['yt'])
    async def youtube_search(self, ctx, *input_query):
        query = ' '.join(word for word in input_query)
        search_results = youtube_call.search(query)
        beginning_link="https://www.youtube.com/watch?v="
        await ctx.channel.send(beginning_link + search_results[0])
     
       
def setup(bot):
    bot.add_cog(GoogleCommands(bot))