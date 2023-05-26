import discord
from discord.ext import commands
from app.config import TOKEN, CHANEL_ID
from discord.ext import tasks
from app.database import db


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)

db_name = "database.db"
user_db = db.UserDatabase(db_name)
solved_table = db.SolvedTable(db_name)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    # create tables
    await db.create_tables(db_name)
    # Load command modules
    await bot.load_extension("app.cmds")

    await bot.wait_until_ready()

    # start task loop
    # from app import tasks
    # tasks.send_task.start()
    send_task.start()


#  loops don't work from separate file because  of discord.py asynchronous architecture,
#  so I put it here
@tasks.loop(hours=24)
async def send_task():
    print(f"Exercises task is on on channel {CHANEL_ID} {type(CHANEL_ID)}")
    channel = bot.get_channel(int(CHANEL_ID))
    print(channel)
    task = await db.get_random_task(db_name)
    if task:
        await channel.send(task["text"])


if __name__ == '__main__':
    bot.run(token=TOKEN)
