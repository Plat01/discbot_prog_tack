from discord.ext import commands
from app.database.db import get_actual_task
from main import solved_table


@commands.command()
async def hello(ctx):
    """Responds with a greeting."""
    await ctx.send(f"Hello, {ctx.author.mention}!")
    print(ctx.author)


@commands.command()
async def solv(ctx):
    """Function test all users solutions"""
    tests = await get_actual_task("database.db")
    correct = True
    if tests[6]:
        if exec(tests[5]) != tests[6]:
            return None
    if tests[3]:
        if exec(tests[3]) != tests[4]:
            return None
    if exec(tests[1]) == tests[2]:
        return solved_table.create_row(ctx.author.mention, tests[0])


@commands.command()
async def ping(ctx):
    await ctx.send("pong")


async def setup(bot):
    bot.add_command(ping)
    bot.add_command(hello)





