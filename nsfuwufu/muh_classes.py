from uuid import uuid4
from typing import List, Optional, Union

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
    
    def __str__(self):
        return self.name if self.name else "Anonyamous." # mine has a nya in it but moose is also funnyAnonyamous
                                                        # oh shit i didn't see
    
    def __repr__(self):
        return self.name if self.name else "Anonymoose." # xD
      
class Manager:
    def __init__(self):
        self.tasks = []
        self.post_interval = 5
        self.artist_list = [
            "Chihunhentai",
            "blue-senpai",
            "leaf98k",
            "zynxy",
            "cutesexyrobutts",
            "pinki_o64",
            "jakko",
            "foxyreine",
            "dishwasher1910",
            "anima_(togashi)",
            "simao_(x_x36131422)",
            "momo_no_sukebe",
            "niliu_chahui",
            "z.taiga",
            "gomashio_ponz",
            "black_mutou",
            "theobrobine"
        ]

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
    def get_post_interval(self):
        return self.post_interval
    
    def set_post_interval(self, interval):
        self.post_interval = int(interval)

    def get_all_artists(self):
        output = ""
        for artist in self.artist_list:
            output += artist + '\n'
        return output


