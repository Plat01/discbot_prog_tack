# from discord.ext import tasks
# from app.config import CHANEL_ID
# from main import bot
#
#
# # function send task every day
# @tasks.loop(hours=24)
# async def send_task():
#     chanel = bot.get_channel(CHANEL_ID)
#     tack = "Sthg"
#     await chanel.send(tack)
#
#
# @bot.event
# async def on_ready():
#     print("Bot is ready")
#     send_task.start()
#
#
# @bot.event
# async def on_member_join(member):
#     pass
#
#
# @bot.command()
# async def hello(ctx):
#     """Responds with a greeting."""
#     await ctx.send(f"Hello, {ctx.author.mention}!")
#     print(ctx.author)


from discord.ext import commands


class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Responds with a greeting."""
        await ctx.send(f"Hello, {ctx.author.mention}!")


def setup(bot):
    bot.add_cog(MyCommands(bot))



