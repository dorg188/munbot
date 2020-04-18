from discord.ext import commands


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot: commands.Bot):
    bot.add_cog(Settings(bot))


def teardown(bot: commands.Bot):
    bot.remove_cog('Settings')
