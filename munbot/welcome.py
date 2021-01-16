import sys
import contextlib
import datetime
import time
import asyncio

import discord
from discord.ext import commands
from munbot.core.conference import Conference
from munbot.core.committee import Committee
from munbot.core.exceptions import MUNException


committees = ['UNICEF', 'GA']


class Welcome(commands.Cog):
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if after and after.channel:
            if after.channel.category and after.channel.category.name in committees:
                if not after.mute:
                    await member.edit(mute=True)
            else:
                if after.mute:
                    await member.edit(mute=False)
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandInvokeError):
        if isinstance(error.original, MUNException):
            await ctx.send(f':x: {error.original}')
        else:
            raise error
    
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
    
    @commands.command('conf')
    async def create_conf_test(self, ctx: commands.Context, conference_name: str):
        self.conf = Conference(conference_name, ctx.guild)
        await ctx.send(f'The {conference_name} conference was created!')
    
    @commands.command('ccomm')
    async def create_new_committee_test(self, ctx: commands.Context, committee_name: str):
        comm = Committee(self.conf, committee_name, [], [])
        await self.conf.register_committee(comm)
    
    @commands.command('rcomm')
    async def delete_committee_test(self, ctx: commands.Context, committee_name: str):
        await self.conf.remove_committee(committee_name)
    
    @commands.command('error')
    async def error_command_test(self, ctx: commands.Context):
        raise ValueError('Some error!')

    @commands.command('embed')
    async def test_embeded_message(self, ctx: commands.Context):
        async with ctx.typing():
            embed = discord.Embed(title='Information', description='This is test for embeded messages')
            embed.add_field(name='Time', value=datetime.datetime.now().isoformat(), inline=False)
            embed.add_field(name='Epoch Time', value=time.time(), inline=False)
            await ctx.send(embed=embed)
            embed = discord.Embed(title='Information', description='This is test for embeded messages with inline fields',
                                  color=discord.Color.blurple())
            embed.add_field(name='Time', value=datetime.datetime.now().isoformat(), inline=True)
            embed.add_field(name='Epoch Time', value=time.time(), inline=True)
            await ctx.send(embed=embed)
    
    @commands.command('echo')
    async def echo_in_dm(self, ctx: commands.Context):
        if not ctx.author.dm_channel:
            await ctx.author.create_dm()
        await ctx.author.dm_channel.send(content=ctx.message.content[ctx.message.content.find(' '):],
                                         files=[await attachment.to_file() for attachment in ctx.message.attachments])
    
    @commands.command('delay')
    async def delayed_message(self, ctx: commands.Context, delay: int):
        message = ctx.message.content[ctx.message.content.find(' ', ctx.message.content.find(' ') + 1):]
        await ctx.send(f'Before: {message} {datetime.datetime.now().isoformat()}')
        await asyncio.sleep(delay)
        await ctx.send(f'After: {message} {datetime.datetime.now().isoformat()}')


def setup(bot: commands.Bot):
    bot.add_cog(Welcome())


def teardown(bot: commands.Bot):
    bot.remove_cog('Welcome')
