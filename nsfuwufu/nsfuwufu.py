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
        fufutask = self.create_fufu_task(ctx, interval=self.fufu_manager.get_post_interval()) #interval=self.fufu_manager.get_post_interval
        if fufutask == None:
            await ctx.send("")

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
                imgurl = imgurl["message"]
            else:
                desc = None
            # change this to go to a booru function that returns an image link 
            embedded_image = await make_embed(my_color, imgurl, desc)
            return embedded_image
    
        async def make_embed(my_color, image, desc):
            if desc is not None:
                em = Embed(color=my_color, description=desc)
            else:
                em = Embed(color=my_color)
            
            em.set_image(url=image)        
            return em

        async def make_embed_for_booru(image):
            em = Embed()            
            em.set_image(url=image)        
            return em

        async def get_img_url(url):        
            response = get(url)            
            return response.json()     

        async def get_booru_img(url): 
            response = get(url)                       
            return response.json() 
        
        @tasks.loop(seconds=interval, reconnect = True)
        async def fufutask(ctx): 
            NEKOBOT_URL = "https://nekobot.xyz/api/image?type={}"
            DANBOORU_URL = "https://danbooru.donmai.us/posts.json?tags={}&random=true&limit=100"
            keyword # to be used later
            coffee = False
            tag_to_get = self.tag_selection[randint(0,len(self.tag_selection)-1)]
            new_urls = None
            embed = None
            if tag_to_get == 'coffee':
                coffee = True
                new_urls = NEKOBOT_URL.format(tag_to_get)
                embed = await get_img_and_embed(
                    self,
                    url=NEKOBOT_URL.format(tag_to_get),
                    post_coffee=coffee
                )
            else:
                artist_list_length = len(self.fufu_manager.artist_list)
                random_artist = self.fufu_manager.artist_list[randint(0,artist_list_length - 1)]
                new_urls = await get_booru_img(DANBOORU_URL.format(random_artist))                
                single_image = new_urls[0]
                for urls in new_urls:
                    # if not "loli" in urls["tag_string"] or not "gore" in urls["tag_string"]:
                    if not "loli" in urls["tag_string"] and not "gore" in urls["tag_string"]:
                        single_image = urls
                        break                                   

                embed = await make_embed_for_booru(image=single_image["file_url"])
                # oops :D, :P
                # await ctx.send("Nya-ho!") 
            await ctx.send(embed=embed)
        please_return_an_object = fufutask.start(ctx)
        return please_return_an_object
        #test
    
    
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

    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    async def set_timer(self, ctx: commands.Context, interval: int):
        # stops the current task
        self.fufu_manager.delete_tasks(ctx.author.id)
        # sets the interval
        self.fufu_manager.set_post_interval(interval)        
        await ctx.send("Task was stopped and interval set to {}".format(interval))

    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    async def get_artists(self, ctx: commands.Context):
        list_of_artists = self.fufu_manager.get_all_artists()
        await ctx.send(list_of_artists)

    @commands.is_owner()
    @commands.is_nsfw()
    @commands.command()
    async def get_version(self, ctx: commands.Context):
        version = self.fufu_manager.get_version()
        await ctx.send(version)

