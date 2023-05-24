import discord
from discord.ext import commands
from app.config import TOKEN
import tracemalloc


tracemalloc.start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    # Load command modules
    await bot.load_extension(name="handlers", package="app")

if __name__ == '__main__':
    bot.run(token=TOKEN)
