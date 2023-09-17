import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix = '!')
 
@bot.event
async def on_ready():
    print ("SNKR WRLD BOT IS READY")

async def react_success(message):
    await message.add_reaction("<:wrldW:823624620347359292>")

async def react_suggestions(message):
    await message.add_reaction("✅")
    await message.add_reaction("❌")

@bot.event                                             
async def on_message(message):
    if message.channel.id == 821936235886673960:
        if message.attachments:
            await react_success(message)
    if message.channel.id == 821938033850449930:
        await react_suggestions(message)

bot.run("NzQ3NjMyNzI2Mjg2MjcwNTY1.X0RtPA.qQYeCrAD6ViCZk2UFy2TCferT4U")
