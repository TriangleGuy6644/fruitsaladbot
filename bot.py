# Imports
import discord
from discord.ext import commands
#ignore ts friggin error, it works
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')
#initialize bot
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

# Event: Bot is ready
@bot.event
async def on_ready():
    print("[FruitSalad]: Online!")


#run bot
bot.run(TOKEN)

