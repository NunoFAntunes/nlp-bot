from threading import Thread
from time import sleep
import sys

async def countdown_recursive(ctx, seconds, timer_type):
    if(seconds == 0):
        await ctx.channel.send("Your timer is up!")
        sys.exit()
    else:
        seconds = seconds-1
        print(seconds)
        if(timer_type == 0):
            if(seconds%15==0):
                await ctx.channel.send('%s seconds remaining!' % str(seconds))
        elif(timer_type == 1):
            if(seconds%60==0):
                await ctx.channel.send('%s minutes remaining!' % str(seconds/60))
            elif(seconds<60 and seconds%15==0):
                await ctx.channel.send('%s seconds remaining!' % str(seconds))
        else:
            if(seconds%3600==0):
                await ctx.channel.send('%s hours remaining!' % str(seconds/3600))
            elif(seconds<3600 and seconds%60==0):
                await ctx.channel.send('%s minutes remaining!' % str(seconds/60))
            elif(seconds<60 and seconds%15==0 and seconds != 0):
                await ctx.channel.send('%s seconds remaining!' % str(seconds))
        sleep(1)
        return await countdown_recursive(ctx, seconds, timer_type)
    
async def start_timer(ctx, seconds, timer_type):
    t1 = Thread(target=countdown_recursive, args=(ctx, seconds, timer_type))
    t1.start() #Calls first function