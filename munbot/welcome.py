import contextlib

import discord
from munbot.core.conference import Conference
from munbot.core.committee import Committee
from discord.ext import commands


committees = ['UNICEF', 'GA']


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if after and after.channel:
            if after.channel.category and after.channel.category.name in committees:
                if not after.mute:
                    await member.edit(mute=True)
            else:
                if after.mute:
                    await member.edit(mute=False)
    
    @commands.command('whoami')
    async def whoami(self, ctx: commands.Context):
        await ctx.send(f':desktop: {ctx.guild.name}\n:hash: {ctx.channel.name}\n:smiley: {ctx.author.name}', delete_after=5)
        await ctx.message.delete()
    
    @commands.command('calc')
    async def calculate(self, ctx: commands.Context, num1: int, num2: int):
        await ctx.send(f'Results:\n'
                       f'{num1} + {num2} = {num1 + num2}\n'
                       f'{num1} - {num2} = {num1 - num2}\n'
                       f'{num1} * {num2} = {num1 * num2}\n'
                       f'{num1} / {num2} = {num1 / num2}')
    
    @commands.command('committee')
    async def create_new_committee_test(self, ctx: commands.Context, committee_name: str):
        conf = Conference('', discord.utils.get(self.bot.guilds, name='vMUN'))
        comm = Committee(conf, committee_name, [], [])
        await comm.initialize_committee()


def setup(bot: commands.Bot):
    bot.add_cog(Welcome(bot))


def teardown(bot: commands.Bot):
    bot.remove_cog('Welcome')
