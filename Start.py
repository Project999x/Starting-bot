import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get values from .env
API_ID = int(os.getenv("API_ID", 19822764))
API_HASH = os.getenv("API_HASH", "b240e413364b8608a542a7cafc6903be")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8311348398:AAGy02UrCSC7eFRTt1lVg0yvuvIxWi7u0Pc")

# Create the bot client
app = Client(
    "MyStarterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ---------- Commands ----------

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIokGj7KoVQcUfF6a9woj9azZOuXIkKAAK5EAACfV4QVMNYFRE0aPt8HgQ")  # random sticker
    await message.reply_text(
        "✨ Hey there!\n\nI'm alive and running perfectly.\nUse /help to see available commands.",
        parse_mode="html"
    )

@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "Available Commands:\n\n"
        "/start - Check if bot is alive\n"
        "/help - Show this help message\n"
        "/info - Get info about the bot\n"
        "/users - (Demo) Show total users\n"
        "/ping - Check bot speed",
        parse_mode="HTML"
    )

@app.on_message(filters.command("info"))
async def info_command(client: Client, message: Message):
    bot_user = await client.get_me()
    await message.reply_text(
        f"🤖 Bot Info:\n\n"
        f"Name: {bot_user.first_name}\n"
        f"Username: @{bot_user.username}\n"
        f"ID: {bot_user.id}",
        parse_mode="HTML"
    )

@app.on_message(filters.command("users"))
async def users_command(client: Client, message: Message):
    await message.reply_text(
        "👥 Currently tracking user count isn’t set up yet.\nYou can add a database later to store user info.",
        parse_mode="HTML"
    )

@app.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message):
    from time import time
    start_time = time()
    sent = await message.reply_text("🏓 Pinging...")
    end_time = time()
    ping_ms = (end_time - start_time) * 1000
    await sent.edit_text(f"✅ Pong! {int(ping_ms)}ms", parse_mode="Markdown")

# ---------- Start Bot ----------
print("🚀 Bot is starting...")
app.run()
print("✅ Bot is running now!")
