from app.config import CHANEL_ID
from discord.ext import tasks
import main


# function send task every "day"
@tasks.loop(seconds=24)
async def send_task():
    print(f"Exercises task is on on channel {CHANEL_ID}")
    chanel = main.bot.get_channel(int(CHANEL_ID))
    # chanel = main.bot.fetch_channel(1094300838580728002)
    # chanel = client.get_channel(746382173)
    tack = "Sthg"
    print(chanel)
    # await channel.send(tack)
