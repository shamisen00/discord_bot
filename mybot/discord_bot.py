import os
from pathlib import Path
from discord.ext import commands
from dotenv import load_dotenv

if __name__ == '__main__':
    env_path = Path.cwd().parent / ".env"

    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

    bot = commands.Bot(command_prefix='!')

    bot.load_extension('cogfile')

    bot.run(TOKEN)