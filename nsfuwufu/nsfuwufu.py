from redbot.core import commands
from discord.ext import tasks
from discord import Embed, Colour
from redbot.core import commands
from linecache import getline
from random import randint
from requests import get
from os import path

from .muh_classes import Manager, Task
from .fufu_exceptions import FufuException



class Fuwu(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        self.fufu_manager = Manager()
        filename = path.join(path.dirname(path.abspath(__file__)), 'bible.txt')
        file = open(filename)
        self.bible = file.readlines()
        file.close()
       
    @commands.command()
    async def fu(self, ctx):
        """This does stuff!"""
        # Your code will go here        
        print(dir(ctx.author))
        await ctx.send("I can do stuff!")
        
    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    # @commands.bot_has_permissions(embed_links=True)
    async def fufustart(self, ctx):
        if not ctx.author.id:
            raise FufuException("Ghost mothefucker trying to run fufutest without a user id.") # xD
        
        fufutask = self.create_fufu_task(ctx, interval=5)
        new_task = Task(ctx.author.id, fufutask, "hell yeah") #over here !
        self.fufu_manager.add_task(new_task)
        await ctx.send("Task started uwu :3")
    
    def create_fufu_task(self, ctx, keyword="hentai", interval=3600):

        async def get_img_and_embed(self, url):
            imgurl = await get_img_url(url)        
            my_color = Colour(int(imgurl["color"])) # taking base 10 int and turning it in to Color type

            # print('message', type(imgurl["message"]), imgurl["message"])
            # print('color', type(my_color), my_color) #dear god dont use print without () you will get banned from github! xD :D
            
            bible_line = self.bible[randint(1,24600)]            
            embedded_image = await make_embed(my_color, imgurl["message"], bible_line)
            return embedded_image
    
        async def make_embed(my_color, image, desc):
            em = Embed(color=my_color, description=desc)
            em.set_image(url=image)        
            return em

        async def get_img_url(url):        
            response = get(url)
            return response.json()     
        
        @tasks.loop(seconds=interval, reconnect = True)
        async def fufutask(ctx): 
            keyword # to be used later

            NEKOBOT_URL = "https://nekobot.xyz/api/image?type={}"
            embed = await get_img_and_embed( #TODO make a getter for tasks under user
                    self,
                    url=NEKOBOT_URL.format("hentai")
            )
            # oops :D, :P
            # await ctx.send("Nya-ho!")            
            await ctx.send(embed=embed)
            
        please_return_an_object = fufutask.start(ctx)
        return please_return_an_object

    @commands.command()
    async def listtasks(self, ctx):        
        await ctx.send(self.fufu_manager.get_all_tasks_by_user(ctx.author.id)) #beat me :P :D

    @commands.command()
    async def fufustop(self, ctx):
        self.fufu_manager.delete_tasks(ctx.author.id)
        await ctx.send("tasks yeeted") #pls  use correct internet terminology
        # my bad   
