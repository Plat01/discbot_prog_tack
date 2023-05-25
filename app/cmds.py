from discord.ext import commands


@commands.command()
async def hello(ctx):
    """Responds with a greeting."""
    await ctx.send(f"Hello, {ctx.author.mention}!")
    print(ctx.author)


@commands.command()
async def ping(ctx):
    await ctx.send("pong")


async def setup(bot):
    bot.add_command(ping)
    bot.add_command(hello)



