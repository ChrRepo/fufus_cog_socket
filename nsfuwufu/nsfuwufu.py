from redbot.core import commands

class Fuwu(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fu(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")