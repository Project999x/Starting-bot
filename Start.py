from pyrogram import Client, filters
import os
import json

# Bot credentials
API_ID = int(os.getenv("API_ID", "19822764"))  # replace with your own
API_HASH = os.getenv("API_HASH", "b240e413364b8608a542a7cafc6903be")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8311348398:AAGy02UrCSC7eFRTt1lVg0yvuvIxWi7u0Pc")

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

USERS_FILE = "users.json"

# Load users
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users_db = json.load(f)
else:
    users_db = {}

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(users_db, f, indent=4)

# Example stickers (replace with your favorite sticker IDs)
START_STICKER = "CAACAgUAAxkBAAIohGj7KiNDCwq7_AF09HZk_WTCar_tAALaAgAC48xIVd0dJb7bHOZJHgQ"
PING_STICKER = "CAACAgUAAxkBAAIohmj7KiSMatHNaJeZ7G_9O2Iy-a2bAALyBQACrydIVU6UOnYuub5THgQ"
HELP_STICKER = "CAACAgUAAxkBAAIokGj7KoVQcUfF6a9woj9azZOuXIkKAAK5EAACfV4QVMNYFRE0aPt8HgQ"

# /start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or message.from_user.first_name
    users_db[user_id] = username
    save_users()

    await message.reply_sticker(START_STICKER)
    text = f"✨ <b>Hello, {username}!</b> ✨\n\nWelcome to <i>My Pyrogram Bot</i> 🤖\nUse /help to see all available commands 📝"
    await message.reply_text(text, parse_mode="html")

# /help command
@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_sticker(HELP_STICKER)
    text = (
        "📜 <b>Available Commands</b> 📜\n\n"
        "/start - Start the bot 🚀\n"
        "/help - Show this help message 📝\n"
        "/users - List all users 👥\n"
        "/info - Bot info ℹ️\n"
        "/ping - Check bot status 🏓"
    )
    await message.reply_text(text, parse_mode="html")

# /users command
@app.on_message(filters.command("users"))
async def users_command(client, message):
    if users_db:
        user_list = "\n".join([f"👤 {uid} - @{uname}" for uid, uname in users_db.items()])
        await message.reply_text(f"<b>Users who interacted with the bot:</b>\n{user_list}", parse_mode="html")
    else:
        await message.reply_text("❌ No users have interacted with the bot yet.", parse_mode="html")

# /info command
@app.on_message(filters.command("info"))
async def info_command(client, message):
    text = (
        "🤖 <b>Bot Info</b> 🤖\n\n"
        "Name: <i>My Pyrogram Bot</i>\n"
        "Language: Python 🐍\n"
        "Framework: Pyrogram ⚡\n"
        "Status: ✅ Running"
    )
    await message.reply_text(text, parse_mode="html")

# /ping command
@app.on_message(filters.command("ping"))
async def ping_command(client, message):
    await message.reply_sticker(PING_STICKER)
    await message.reply_text("🏓 Pong! Bot is alive!")

# Run the bot
if __name__ == "__main__":
    print("✨ Bot started... ✨")
    app.run()
