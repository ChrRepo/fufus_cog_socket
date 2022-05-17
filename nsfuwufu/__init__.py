from .nsfuwufu import Fuwu
from redbot.core.bot import Red



__red_end_user_data_statement__ = (
    "This cog does not persistently work to any degree of satisfaction\
    but you might see catgirls so grin and eat the turd sandwhich."
)


def setup(bot: Red):
    cog = Fuwu(bot)
    bot.add_cog(cog)