import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix = '!')
 
@bot.event
async def on_ready():
    print ("SNKR WRLD BOT IS READY")

async def react(message):
    #await message.add_reaction("<:ihateleo:818701078265724938>")
    await message.add_reaction("<:wrldW:823624620347359292>")

@bot.event                                             
async def on_message(message):
    if message.channel.id == 821936235886673960:
        if message.attachments:
            await react(message)

bot.run("NzQ3NjMyNzI2Mjg2MjcwNTY1.X0RtPA.qQYeCrAD6ViCZk2UFy2TCferT4U")

# copy and paste everything above this line
# everything below this is just an example of what final code could/would/should look like
