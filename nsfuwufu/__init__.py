from .nsfuwufu import Fuwu
from redbot.core.bot import Red


__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


def setup(bot: Red):
    cog = Fuwu(bot)
    bot.add_cog(cog)