import asyncio

import discord
from discord.ext import commands
from app.config import TOKEN
# from app import tasks, cmds, events
# import tracemalloc
#
# tracemalloc.start()


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    # Load command modules
    await bot.load_extension("app.cmds")
    # await bot.wait_until_ready()
    # tasks.send_task.start()
    channel = bot.get_channel(1094300838580728002)
    print(channel)
    send_task.start()
    # await channel.send("sqwe")



@bot.event
async def on_shard_resumed(shard_id):
    print(f"Shard {shard_id} has resumed.")
# @bot.event
# async def on_shard_ready(1094300838580728002):
#     tasks.send_task.start()


if __name__ == '__main__':
    from discord.ext import tasks


    @tasks.loop(seconds=24)
    async def send_task():
        print(f"Exercises task is on on channel ")
        channel = bot.get_channel(1094300838580728002)
        tack = "Sthg"
        print(channel)
        await channel.send(tack)


    bot.run(token=TOKEN)
