import discord
from discord.ext import commands
from app.config import TOKEN


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    # Load command modules
    await bot.load_extension("app.cmds")
    # start task loop
    send_task.start()


if __name__ == '__main__':
    from discord.ext import tasks

    #  loops don't work from separate file because  of discord.py asynchronous architecture,
    #  so I put it here
    @tasks.loop(seconds=24)
    async def send_task():
        print(f"Exercises task is on on channel ")
        channel = bot.get_channel(1094300838580728002)
        tack = "Sthg"
        print(channel)
        await channel.send(tack)


    bot.run(token=TOKEN)
