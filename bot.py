import discord
from discord.ext import commands
from mod import check_profanity
import os
from dotenv import load_dotenv
from key import generate_key

# ✅ Load .env variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

SESSION_KEY = generate_key()

# ✅ Load admin IDs from .env
ADMIN_IDS = [int(admin.strip()) for admin in os.getenv("ADMIN_IDS").split(",")]


print(f"SESSION KEY: {SESSION_KEY}")
print(f"Hello, Admins: {ADMIN_IDS}, you will get the KEY into your DM's shortly.")

# ✅ on_ready: DM admins + public announce
@bot.event
async def on_ready():
    print(f"✅ Smriti is online as {bot.user}")

    # Send session key to all admins via DM
    for admin_id in ADMIN_IDS:
        try:
            admin_user = await bot.fetch_user(admin_id)
            await admin_user.send(f"Bot is Online, Session Key will be sent Shortly")
            await admin_user.send(f"Session key is: {SESSION_KEY}")
            print(f"✅ Sent session key to admin {admin_id}")
        except Exception as e:
            print(f"❌ Failed to DM admin {admin_id}: {e}")

# ✅ Profanity and help handling for normal messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_message = message.content.lower()

    if message.content.startswith('!'):
        await bot.process_commands(message)
        return

    if check_profanity(user_message):
        await message.channel.send("Abstain from using profanity, please.")
        print(f"[PROFANITY] {message.author} used: {user_message}")
        return

    if user_message == 'help':
        embed = discord.Embed(
            title="Bhagavad Gita Bot",
            url="https://bhagavadgita.io/",
            color=0x00ff00
        )
        embed.add_field(name="hello / bye", value="Bot responds with blessings.", inline=False)
        embed.add_field(name="random", value="Generates a random Bhagavad Gita verse.", inline=False)
        embed.add_field(name="verse <x>.<y>", value="Fetch a specific verse.", inline=False)
        await message.channel.send(embed=embed)
        return

    await bot.process_commands(message)

# ✅ Commands
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def radiance(ctx):
    print(f"Oppenheimer Quote")
    await ctx.send("\"Now I am Become Death, the Destroyer of Worlds\"")

@bot.command()
async def shutdown(ctx, key1: str = ""):
    if key1 != SESSION_KEY:
        await ctx.send("🔒 Incorrect key. Nice try.")
        return
    print(f"Bot Shutting down, as per admin command. please check and inquire if this was excecuted by non-admins.")
    await ctx.send("Shutting down...")
    await bot.close()

@bot.command()
async def testprofanity(ctx, *, message):
    if check_profanity(message):
        await ctx.send("⚠️ Profanity detected.")
    else:
        await ctx.send("✅ No profanity detected.")

# ✅ Run bot
bot.run(os.getenv("DISCORD_TOKEN"))


#100 lines of code! uwu 