import sqlite3


class SQLiter:
    def __int__(self):
        self.connect = sqlite3.connect("data.slite3")
        self.cursor = self.connect.cursor()