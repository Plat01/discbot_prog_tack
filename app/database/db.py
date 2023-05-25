import asyncio

import aiosqlite

if __name__ == '__main__':
    async def main():
        async with aiosqlite.connect("../../database.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS test(id integer)")
                await cursor.commit():


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
