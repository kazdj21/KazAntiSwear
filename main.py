import difflib
from discord.ext import commands
import re

bot = commands.Bot(command_prefix="$")

with open("token.txt", "r") as file:
    token = file.readline()

def censorCheck(userInput):
    with open("swear-list.txt", "r") as file:
        wordList = file.read().split()
        wordList.sort()
    replacing = re.sub("[-/?<>;'~!@#$%^&*()]", " ", userInput)
    userInputList = replacing.split()
    for word in userInputList:
        for item in wordList:
            a = item
            b = word
            seq = difflib.SequenceMatcher(None, a, b).ratio() * 100
            if seq > 80:
                return True

    return False



@bot.event
async def on_message(message):

    if censorCheck(message.content):
        await message.delete()
        await message.channel.send("You cannot swear here!")

@bot.command
async def warn(ctx):
    await ctx.send("You cannot swear here!")

bot.run(token)
