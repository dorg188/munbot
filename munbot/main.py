import os
import signal
import logging
import discord.ext.commands
from dotenv import load_dotenv
import multiprocessing
import IPython
from traitlets.config.loader import Config

logging.basicConfig(level=logging.INFO)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.ext.commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print('MUNBot ONLINE!')


def main():
    bot.load_extension('welcome')
    bot.load_extension('flags')
    bot_process = multiprocessing.Process(target=bot.run, args=[TOKEN], name='MUNBot Process')
    bot_process.start()
    IPython.start_ipython(
        user_ns={'bot': bot},
        config=Config(TerminalInteractiveShell={'banner1': 'MUNBot Interactive'})
    )
    os.kill(bot_process.pid, signal.SIGINT)
    bot_process.join()


if __name__ == "__main__":
    main()
