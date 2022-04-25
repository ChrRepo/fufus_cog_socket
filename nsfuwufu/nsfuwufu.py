from redbot.core import commands
from discord.ext import tasks

from .muh_classes import Manager, Task
from .fufu_exceptions import FufuException




class Fuwu(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.fufu_manager = Manager()
       
    @commands.command()
    async def fu(self, ctx):
        """This does stuff!"""
        # Your code will go here        
        print(dir(ctx.author))
        await ctx.send("I can do stuff!")
        
    @commands.command()
    async def fufutest(self, ctx):
        if not ctx.author.id:
            raise FufuException("Ghost mothefucker trying to run fufutest without a user rid.") # xD
        
        fufutask = self.create_fufu_task(ctx, interval=4)
        new_task = Task(ctx.author.id, fufutask, "hell yeah") #over here !
        self.fufu_manager.add_task(new_task)

        await ctx.send("Task started uwu :3")
    
    def create_fufu_task(self, ctx, keyword="hentai", interval=5):

        @tasks.loop(seconds=interval, reconnect = True)
        async def fufutask(ctx): 
            keyword # to be used later

            await ctx.send("Nya-ho!")
            
        please_return_an_object = fufutask.start(ctx)
        return please_return_an_object

    @commands.command()
    async def listtasks(self, ctx):        
        await ctx.send(self.fufu_manager.get_all_tasks_by_user(ctx.author.id)) #beat me :P :D

    @commands.command()
    async def deletetasks(self, ctx):
        self.fufu_manager.delete_tasks(ctx.author.id)
        await ctx.send("tasks yeeted") #pls  use correct internet terminology
        # my bad
