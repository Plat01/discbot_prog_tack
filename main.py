import discord
from discord.ext import commands
from app.config import TOKEN, CHANEL_ID
from discord.ext import tasks


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    # Load command modules
    await bot.load_extension("app.cmds")

    await bot.wait_until_ready()

    # start task loop
    # from app import tasks
    # tasks.send_task.start()
    send_task.start()


@bot.event
async def on_message(message):
    # Check if the message author is a member of a guild (server)
    if message.guild:
        member = message.guild.get_member(message.author.id)
        if member:
            # Accessing member information
            username = member.name  # Username of the member
            nickname = member.nick  # Nickname of the member (if set)
            discriminator = member.discriminator  # Member's discriminator
            # avatar_url = member.avatar_url  # URL of the member's avatar
            joined_at = member.joined_at  # Date and time the member joined the server
            roles = member.roles  # List of roles the member has
            permissions = member.guild_permissions  # Member's permissions in the server

            # Printing member information
            print(f"Username: {username}")
            print(f"Nickname: {nickname}")
            print(f"Discriminator: {discriminator}")
            print(f"Joined At: {joined_at}")
            print(f"Roles: {roles}")
            print(f"Permissions: {permissions}")


#  loops don't work from separate file because  of discord.py asynchronous architecture,
#  so I put it here
@tasks.loop(seconds=24)
async def send_task():
    print(f"Exercises task is on on channel {CHANEL_ID} {type(CHANEL_ID)}")
    channel = bot.get_channel(int(CHANEL_ID))
    print(channel)
    # await channel.send(tack)


if __name__ == '__main__':

    bot.run(token=TOKEN)
