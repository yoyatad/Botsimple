import discord
import time
import asyncio
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='?', help_command=None)
token = ''#ปล่อยว่างไว้

@bot.event
async def on_ready() :
    print("? Started")
@bot.event
async def on_message(message) :
    await bot.process_commands(message)
@bot.command()
async def start(ctx) :
    await ctx.send('OK')
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Command", color=0xef8206)
    embed.set_thumbnail(url="https://img.icons8.com/emoji/2x/question-mark-emoji.png")
    embed.add_field(name="`?help`", value="คำสั่งต่างๆ", inline=True)
    embed.add_field(name="`?quiz <ตัวเลข>`", value="เลือกข้อที่จะทำ", inline=False)
    embed.add_field(name="`ตัวเลข`", value="1-10", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def categories(ctx):
    embed=discord.Embed(title="Categories", color=0xef8206)
    embed.add_field(name="หมวดหมู่", value=categories_str)
    await ctx.send(embed=embed)
emojinum = {1:"1️⃣", 2:"2️⃣", 3:"3️⃣", 4:"4️⃣", 5:"5️⃣", 6:"6️⃣", 7:"7️⃣", 8:"8️⃣", 9:"9️⃣", 10:"🔟"}
allquiz = {"1": ("What was the name of the Ethiopian Wolf before they knew it was related to wolves?", 
                ("Simien Jackel", True), 
                ("Ethiopian Coyote", False), 
                ("Amharic Fox", False), 
                ("Canis Simiensis", False), 
                {'True':"1️⃣"}), 
            "2": ("What scientific suborder does the family Hyaenidae belong to", 
                ("Haplorhini", False), 
                ("Feliformia", True), 
                ("Ciconiiformes", False),
                ("Caniformia", False),
                {'True':"2️⃣"})}
@bot.command()
async def quiz(ctx, number) :
    await ctx.send(f'OK {ctx.author.mention}')
    embed=discord.Embed(title=f"Question {number}", color=0xef8206)
    newstr = ""
    num = 1
    state = False
    for x in allquiz[number]:
        if len(x) == 2:
            newstr += f"{num} {x[0]}\n\n"
            num += 1
    embed.add_field(name=allquiz[number][0], value=newstr, inline=True)
    embed.set_footer(text="Time: 15 seconds")
    question = await ctx.send(embed=embed)
    await question.add_reaction("1️⃣")
    await question.add_reaction("2️⃣")
    await question.add_reaction("3️⃣")
    await question.add_reaction("4️⃣")
    def check(reaction, user):
        return user == ctx.author and reaction.message.id == question.id and str(reaction.emoji) == (allquiz[number][5]).get('True')
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
    except:
        await ctx.channel.send("หมดเวลาครับ")
    else:
        await ctx.channel.send(":white_check_mark: ตอบถูก")
    
    
    
    bot.run(token)
