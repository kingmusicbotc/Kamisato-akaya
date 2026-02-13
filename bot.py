from pyrogram import Client, idle
import logging
from config import API_ID, API_HASH, BOT_TOKEN, PLUGINS_ROOT

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
)

log = logging.getLogger("AyakaBot")

app = Client(
    name="ayaka",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=PLUGINS_ROOT)
)

if __name__ == "__main__":
    log.info("Starting Kamisato Ayaka Bot...")
    app.start()
    log.info("Ayaka is online ❄️")
    idle()
    app.stop()
    log.info("Ayaka is offline.")
