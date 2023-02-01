from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/56d1760224589ee370186.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph//file/e2a332c4222fb05aa14ae.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Lost3oy")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/my_gif_world")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5034422341").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
