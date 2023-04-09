from pyrogram import Client, filters,types
from dotenv import load_dotenv
import os


load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
api_hash = os.getenv('API_HASH')
api_id = os.getenv('API_KEY')


# Create a new Pyrogram client
app = Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    app.send_message(message.chat.id,"hello wellcome to this bot /n ")

# Run the bot
app.run()
