import os
import asyncio
import logging
import discord.ext.commands
from dotenv import load_dotenv
import atexit

logging.basicConfig(level=logging.INFO)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.ext.commands.Bot(command_prefix='mun>')


@bot.event
async def on_ready():
    print('MUNBot ONLINE!')


def main():
    atexit.register(lambda: asyncio.run(bot.close()))
    bot.load_extension('munbot.welcome')
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
