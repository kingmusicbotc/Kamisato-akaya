import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 123456))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Bot Info
BOT_NAME = "Kamisato Ayaka"
BOT_USERNAME = "AyakaBot"

# Owners
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))

# Database (future)
MONGO_URL = os.getenv("MONGO_URL", "")

# Plugins root
PLUGINS_ROOT = "plugins"
