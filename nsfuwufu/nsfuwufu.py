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
        self.tag_selection = ["hentai", "hentai", "hentai", "hentai", "hentai",\
             "hentai", "hentai", "hentai", "hentai", "hentai", "hentai", "hentai", "hentai",  "hentai", "coffee"]
               
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
        if len(self.fufu_manager.tasks) != 0:
            raise FufuException("Tried to run !fufustart but a task is already running.")
        fufutask = self.create_fufu_task(ctx, interval=self.fufu_manager.get_post_interval()) #7200
        new_task = Task(ctx.author.id, fufutask, "hell yeah") #over here !
        self.fufu_manager.add_task(new_task)
        await ctx.send("Task started uwu :3")
    
    def create_fufu_task(self, ctx, keyword="hentai", interval=3600):

        async def get_img_and_embed(self, url, post_coffee):
            imgurl = await get_img_url(url)        
            my_color = Colour(int(imgurl["color"])) # taking base 10 int and turning it in to Color type

            # print('message', type(imgurl["message"]), imgurl["message"])
            # print('color', type(my_color), my_color) #dear god dont use print without () you will get banned from github! xD :D
            if post_coffee:
                desc = self.bible[randint(1,24600)]
            else:
                desc = None
            embedded_image = await make_embed(my_color, imgurl["message"], desc)
            return embedded_image
    
        async def make_embed(my_color, image, desc):
            if desc is not None:
                em = Embed(color=my_color, description=desc)
            else:
                em = Embed(color=my_color)
            
            em.set_image(url=image)        
            return em

        async def get_img_url(url):        
            response = get(url)
            return response.json()     
        
        @tasks.loop(seconds=interval, reconnect = True)
        async def fufutask(ctx): 
            keyword # to be used later
            coffee = False
            tag_to_get = self.tag_selection[randint(0,len(self.tag_selection)-1)]
            if tag_to_get == 'coffee':
                coffee = True

            NEKOBOT_URL = "https://nekobot.xyz/api/image?type={}"
            embed = await get_img_and_embed(
                    self,
                    url=NEKOBOT_URL.format(tag_to_get),
                    post_coffee=coffee
            )
            # oops :D, :P
            # await ctx.send("Nya-ho!")            
            await ctx.send(embed=embed)
            
        please_return_an_object = fufutask.start(ctx)
        return please_return_an_object
    
    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    async def listtasks(self, ctx):        
        await ctx.send(self.fufu_manager.get_all_tasks_by_user(ctx.author.id)) #beat me :P :D

    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    async def fufustop(self, ctx):
        if ctx.author.id != 873878399255449670:
            raise FufuException("Someone tried !fufustop who is not salt. Salt's bot salts rules.")
        self.fufu_manager.delete_tasks(ctx.author.id)
        await ctx.send("tasks yeeted") #pls  use correct internet terminology
        # my bad   

    @commands.command()
    async def set_timer(self, ctx: commands.Context, interval: int):
        # stops the current task
        self.fufu_manager.delete_tasks(ctx.author.id)
        # sets the interval
        self.fufu_manager.set_post_interval(interval)        
        await ctx.send("Task was stopped and interval set to {}".format(interval))
        