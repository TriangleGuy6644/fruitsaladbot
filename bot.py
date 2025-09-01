# Imports
import discord
from discord.ext import commands
#ignore ts friggin error, it works
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')


import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)  

#load cogs from cogs/
for root, dirs, files in os.walk("./cogs"):
    for file in files:
        if file.endswith(".py"):
            # Convert path to module path: cogs/games/dice.py → cogs.games.dice
            path = os.path.join(root, file)
            module = path.replace(os.sep, ".").replace(".py", "")
            bot.load_extension(module)


#run bot
bot.run(TOKEN)
