import discord
from discord.ext import commands
from discord_slash import SlashCommand
from datetime import datetime, timedelta
import operator
import os
from dotenv import load_dotenv
import sqlite3

# Load environment variables
load_dotenv()

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(client)

# Connect to SQLite database
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        entry_count INTEGER DEFAULT 0,
        last_call_time TIMESTAMP
    )
''')
conn.commit()

# Dictionary of messages per channel
channel_messages = {}
for i in range(1, 11):  # Limit of 10 channels
    channel_env = f'CHANNEL_{i}'
    channel_id = os.getenv(channel_env)
    if channel_id:
        channel_messages[channel_id] = "{member.name} is in {channel_name}"
    else:
        break  # Stop the loop if there are no more defined channels

# Variable to control the state of sending messages when someone enters a call
send_message_enabled = True

# Check if logs should be displayed
show_log = os.getenv('SHOW_LOG', 'false').lower() == 'true'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Katchau!"))
    print('Bot online!')
    print(f'Connected as {client.user.name}')
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    global send_message_enabled

    if not send_message_enabled:
        return

    if before.channel == after.channel:
        return  # Ignore updates that don't involve channel changes

    if after.channel:
        if len(after.channel.members) == 1:
            channel = client.get_channel(int(os.getenv('NOTIFICATION_CHANNEL')))
            await channel.send(f"{member.name} is in {after.channel.name}")

            # Update entry count and last call time in the database
            cursor.execute('''
                INSERT OR REPLACE INTO users (id, name, entry_count, last_call_time)
                VALUES (?, ?, COALESCE((SELECT entry_count FROM users WHERE id = ?) + 1, 1), ?)
            ''', (member.id, member.name, member.id, datetime.now()))
            conn.commit()

            if show_log:
                print(f"{member.name} entered a channel.")
        else:
            cursor.execute('SELECT last_call_time FROM users WHERE id = ?', (member.id,))
            result = cursor.fetchone()
            last_call_time = datetime.fromisoformat(result[0]) if result else datetime.min
            if datetime.now() - last_call_time >= timedelta(minutes=60):
                cursor.execute('UPDATE users SET last_call_time = ? WHERE id = ?', (datetime.now(), member.id))
                conn.commit()
                channel = client.get_channel(1206713130353295450)
                if not before.channel:
                    await channel.send(f"{member.mention} is in the call! @here")
    
    if before.channel and after.channel and before.channel != after.channel and show_log:
        print(f"{member.name} was moved from {before.channel.name} to {after.channel.name}")

@slash.slash(name="leaders", description="Shows how many times each user entered calls.")
async def leaders(ctx):
    cursor.execute('SELECT id, name, entry_count FROM users ORDER BY entry_count DESC LIMIT 10')
    leaderboard = cursor.fetchall()
    leaderboard_text = "Entry Leaderboard:\n"
    for idx, (user_id, name, count) in enumerate(leaderboard, start=1):
        leaderboard_text += f"{idx}. {name}: {count} times\n"
    await ctx.send(content=leaderboard_text)
    if show_log:
        print('Leaderboard command executed.')

@slash.slash(name="toggle", description="Turns on/off the functionality of sending a message when someone enters a call.")
async def toggle_message(ctx):
    global send_message_enabled
    send_message_enabled = not send_message_enabled
    status = "enabled" if send_message_enabled else "disabled"
    await ctx.send(content=f"Functionality to send a message when someone enters a call is now {status}.")

@slash.slash(name="help", description="Get a list of commands.")
async def help(ctx):
    commands = [
        "/leaders - Shows how many times each user entered calls.",
        "/toggle - Turns on/off the functionality of sending a message when someone enters a call.",
        "/help - Get a list of commands."
    ]
    command_list = "\n".join(commands)
    await ctx.send(content=f"Hello, {ctx.author.name}! Here's the list of available commands:\n\n{command_list}")

# Load the bot token from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Bot token not found. Make sure to set the DISCORD_BOT_TOKEN environment variable.")

client.run(TOKEN)
