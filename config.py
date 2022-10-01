## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAB4kGvkmdzvxWnRUbOFkqVUrTe32jgNixfLgmoKv2sjOvrZjbqTr-VbgtyxqS0eEcUc3tN4qYXj-cUPybfGy7aJnNixZa65_-4ecFpwkvo193zf6KWZJA4Vgxaygmg49wN5FUVCK7yfQlBx5ZzcT7mi8rSevz8aPo6GrHg5CuCXy5Za3baYdtuLt96KR5u35G5XKZiM3nfdKziFf8Uyee7J-YuahLPNvbr83rRMTY_O6J5XjyYGWNHl6Dz27FNoxc6egOmV3UfZHeICpKgiY8_3Mp9E1BMALGspb7szm9L3nqZ3DuvzwZbYJwHi8E5jiZxSkm_20PPseOpl-I_3FPFwAAAAAVX1iBcA")
BOT_TOKEN = getenv("BOT_TOKEN", "2132657853:AAFBm33kOuipxzHutJesPYYmmoO1tTqxRls")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "9495729"))
API_HASH = getenv("API_HASH", "8a9aeb1762f724d591977b5dee4ad42c")
OWNER_NAME = getenv("OWNER_NAME", "mesho")
OWNER_USERNAME = getenv("OWNER_USERNAME", "m_e_s_h_o")
ALIVE_NAME = getenv("ALIVE_NAME", "tlashany")
BOT_USERNAME = getenv("BOT_USERNAME", "allllosabot")
OWNER_ID = getenv("OWNER_ID", "1923931101")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TLASHANY_MUSIC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "m_o_mol")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "m_o_mol")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1923931101").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", " ").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Meshohhgvhb/music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/1838d6ee695608a4fff29.jpg")
