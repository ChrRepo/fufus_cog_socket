from redbot.core import commands
from discord.ext import tasks

@tasks.loop(seconds=5, reconnect = True)
async def fufutask(ctx): 
    print("Nya-ho!")
    await ctx.send("Nya-ho!")

class Fuwu(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        # channel_id = My_Channel_ID_Here
        # channel = self.bot.get_channel(channel_id)
       
    @commands.command()
    async def fu(self, ctx):
        """This does stuff!"""
        # Your code will go here
        
        await ctx.send("I can do stuff!")
        
    @commands.command()
    async def fufutest(self, ctx):
        # fufutask.cancel()
        fufutask.start(ctx)
        await ctx.send("Task started uwu :3")
    