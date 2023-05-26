import asyncio
import aiosqlite


async def create_tables(db):
    async with aiosqlite.connect(db) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id   TEXT PRIMARY KEY
                               UNIQUE
                               NOT NULL,
                is_active INTEGER NOT NULL
                               DEFAULT (0)
            );
            """
        )
        await db.commit()
        print("Table 'users' is created")

        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                task_id      INTEGER PRIMARY KEY
                                     UNIQUE,
                is_given     INTEGER NOT NULL
                                     DEFAULT (0),
                text         TEXT    NOT NULL
                                     UNIQUE,
                test1_input  TEXT    NOT NULL,
                test1_output TEXT    NOT NULL,
                test2_input  TEXT,
                test2_output TEXT,
                test3_input  TEXT,
                test3_output TEXT,
                is_actual     INTEGER NOT NULL
                                      DEFAULT (0)
            );
            """
        )
        await db.commit()
        print("Table 'tasks' is created")

        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS solved (
                user  REFERENCES users (user_id) ON DELETE NO ACTION
                                                 ON UPDATE CASCADE
                      NOT NULL,
                task  REFERENCES tasks (task_id) 
            );
            """
        )
        await db.commit()
        print("Table 'solved' is created")


async def get_random_task(db):
    """
    Function give random unsent task from task table, and
    set value 1 to column ig_given then. And finally set
    in column "is_actual" 1 to this row and 0 in all others .
    :param db: name of database
    :return: task id and text fo current task if there are unsent tasks in table, otherwise return none
    """
    async with aiosqlite.connect(db) as conn:
        cursor = await conn.cursor()

        # Start a transaction
        await cursor.execute("BEGIN TRANSACTION")

        # Select a random unsent task
        await cursor.execute(
            "SELECT task_id, text FROM tasks WHERE is_given = 0 ORDER BY RANDOM() LIMIT 1"
        )
        task = await cursor.fetchone()
        if task:
            task_id, text = task

            # Update the is_given column to 1 for the selected task
            await cursor.execute(
                "UPDATE tasks SET is_given = 1 WHERE task_id = ?",
                (task_id,)
            )

            # Set is_actual to 1 for the selected task and 0 for all other tasks
            await cursor.execute("UPDATE tasks SET is_actual = 0")
            await cursor.execute("UPDATE tasks SET is_actual = 1 WHERE task_id = ?", (task_id,))

            # Commit the transaction
            await conn.commit()
            return {
                "task_id": task_id,
                "text": text
            }
        else:
            # Rollback the transaction if no unsent tasks are available
            await conn.rollback()
            return None


async def get_actual_task(db):
    async with aiosqlite.connect(db) as conn:
        async with conn.cursor() as cursor:
            cursor.execute("SELECT task_id, test1_input,test1_output, "
                           "test2_input, test2_output, test3_input, test3_output "
                           "FROM tasks WHERE is_actual = 1")
            return


class UserDatabase:
    def __init__(self, db_name):
        self.db_name = db_name

    async def create_user(self, user_id, is_active):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(
                "INSERT INTO users (user_id, is_active) VALUES (?, ?)",
                (user_id, is_active)
            )
            await db.commit()

    async def get_user(self, user_id):
        async with aiosqlite.connect(self.db_name) as db:
            cursor = await db.execute(
                "SELECT * FROM users WHERE user_id = ?",
                (user_id,)
            )
            return await cursor.fetchone()

    async def update_user(self, user_id, is_active):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(
                "UPDATE users SET is_active = ? WHERE user_id = ?",
                (is_active, user_id)
            )
            await db.commit()

    async def delete_user(self, user_id):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(
                "DELETE FROM users WHERE user_id = ?",
                (user_id,)
            )
            await db.commit()


class SolvedTable:
    def __init__(self, db_name):
        self.db_name = db_name

    async def create_row(self, user_id, task_id):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(
                "INSERT INTO solved (user, task) VALUES (?, ?)",
                (user_id, task_id)
            )
            await db.commit()

    async def delete_row(self, user_id, task_id):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(
                "DELETE FROM solved WHERE user = ? AND task = ?",
                (user_id, task_id)
            )
            await db.commit()


async def test(db: str):
    user_db = UserDatabase(db)
    solved_table = SolvedTable(db)

    await user_db.create_user("user123", True)
    user = await user_db.get_user("user123")
    print(user)  # Example output: ('user123', 1)

    await user_db.update_user("user123", False)
    updated_user = await user_db.get_user("user123")
    print(updated_user)  # Example output: ('user123', 0)

    await user_db.delete_user("user123")
    deleted_user = await user_db.get_user("user123")
    print(deleted_user)  # Example output: None

    await solved_table.create_row("user123", 1)
    await solved_table.create_row("user123", 2)

    await solved_table.delete_row("user123", 1)


if __name__ == '__main__':
    db_name = "../../database.db"
    asyncio.run(test(db_name))
