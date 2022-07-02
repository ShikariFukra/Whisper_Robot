import os

#Why coder's say I am Shikarii
# Config Vars
NULLAPI_HASH = "f12a930e7cd670229d9059755c4ea10b"
NULLAPI_KEY = 10518826
NULLBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Shikari Robot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: ShikariRobot
NULL_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text
START_TEXT = f"**✨Heya,there I am a {NULLBOT_NAME}!✨**\n\n💐Type /help to see how to use me!💐\n💐Type /repo to deploy your own bot like {NULLBOT_NAME}💐.\n Powered by ❤️[Shikarii]❤️(https://t.me/ShikariSupportNetwork)"

HELP_TEXT = f"**• ✨How to use {NULLBOT_NAME}✨:**\n\n💐Click the button below OR\n\nType __{BOT_USERNAME} wspr <username> | <text>__\n\nExample: `{BOT_USERNAME} wspr @The_Shikarii | Hello!`\nShikari sir"

REPO_TEXT = f"✨Click the button below to deploy bot like {NULLBOT_NAME}✨ 🌸Thankyou🌸"
