from os import remove
from pydoc import describe
from tracemalloc import start, stop
from uuid import uuid4
from requests import get
from typing import List, Optional, Union
from discord import Embed, Colour
from redbot.core import commands
from linecache import getline
from random import randint

from .fufu_exceptions import FufuException



class Task:
    def __init__(self, user_id, task, name=None):
        if not user_id or not task:
            #print("[Task]Tried to create a task with no user id or task passed through")
            raise FufuException("Hey numnuts you forgot to enter an id and pass it a task.")

        self.id = uuid4()
        self.user_id = user_id
        self.name = name
        self.task_object = task

        print("I have made a task")
        #self.active = False
        
    def cancel(self):
        # here we gotta stop the discord task first
        self.task_object.cancel()
        del self.task_object
        print("i have stopped this task")
    
    async def get_img_and_embed(self, url):
        imgurl = await self.get_img_url(url)        
        my_color = Colour(int(imgurl["color"])) # taking base 10 int and turning it in to Color type        

        # print('message', type(imgurl["message"]), imgurl["message"])
        # print('color', type(my_color), my_color) #dear god dont use print without () you will get banned from github! xD :D
        bible_line = getline('bible.txt', randint(1,24600))
        embedded_image = await self.make_embed(my_color, imgurl["message"], bible_line)
        return embedded_image
    
    async def make_embed(self, my_color, image, desc):
        em = Embed(color=my_color, title='\u200b', description=desc)
        em.set_image(url=image)        
        return em

    async def get_img_url(self, url):        
        response = get(url)
        return response.json()
        

    def __str__(self):
        return self.name if self.name else "Anonyamous." # mine has a nya in it but moose is also funnyAnonyamous
                                                        # oh shit i didn't see
    
    def __repr__(self):
        return self.name if self.name else "Anonymoose." # xD
      
class Manager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def stop_all_tasks(self):
        for task in self.tasks:
            task.cancel() # this might be cancel(), we gotta check discord docs!

    def delete_task():
        pass

    def get_all_tasks_by_user(self, user):
        output = []
        for task in self.tasks:
            if task.user_id == user:
                output.append(task)
        return output
    
    def delete_tasks(self, user):
        for index, task in enumerate(self.tasks):
            if task.user_id == user:
                task.cancel() #? looks good
                # how about we stop task first? :D
                # oh yeah
                # in here though xD
                del self.tasks[index] #this should do it, noice but i thought the python dev was against indexs? well usually yeah but not always
                # and even when they are it's stupid, indexes are super helpful
                # if u want u can change it though
                # nah i like indexes, just going wtih_convetion :P
                # ah, idk if this is actually a conveniton, convention is more for code formatting stuff not actual logic
                # or, I'm sure there's conventions for logic as well, but enumerate is a pretty pythonic thing
                # wakarimashta sensei
        # haha I saw that!
        # hush

