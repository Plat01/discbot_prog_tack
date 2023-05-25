from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")
CHANEL_ID = os.getenv("CHANEL_ID")
SERVER_ID = os.getenv("SERVER_ID")


