# import discord
# from discord.ext import commands
# import datetime
#
# from urllib import parse, request
# import re
#
# bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")
#
# @bot.command()
# async def ping(ctx):
#    await ctx.send('!!acount')
#
#
# @bot.command()
# async def info(ctx):
#        embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
#     embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
#     embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
#        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
#        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
#     embed.set_thumbnail(url=f"{ctx.guild.icon}")
#        embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
#
#    await ctx.send(embed=embed)
#
# @bot.command()
# async def youtube(ctx, *, search):
#        query_string = parse.urlencode({'search_query': search})
#        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
#     search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
#     print(search_results)
#     await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
#
# @bot.event
# async def on_ready():
#        await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
#     print('My Ready is Body')
#
#
# @bot.listen()
# async def on_message(message):
#       if "tutorial" in message.content.lower():
#        await message.channel.send('This is that you want http://youtube.com/fazttech')
#   await bot.process_commands(message)

# bot.run('token')


import discord
import random
from discord.ext import commands

client = discord.Client()

x = 0
b = 0
g = random.randint(1,100)
e = random.randint(1,100)


bot = commands.Bot(command_prefix='!')


@bot.command()
async def ala(ctx):
    await ctx.send(g)

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def ping(ctx):
 await ctx.send('!pong')

@bot.command()
async def pong(ctx):
  await ctx.send('ping')

@bot.command()
async def spam(ctx):
  await ctx.send('You want do it ?')

@bot.command()
async def name(ctx):
  await ctx.send('My name is Cripto')

@bot.command()
async def no(ctx):
  await ctx.send('OK')

@bot.command()
async def yes(ctx):
   for i in range(0,11):
     await ctx.send('spam')

@bot.command()
async def lol(ctx):
  for i in range(0,11):
        await ctx.send('spam')

@bot.command()
async def er(ctx):
  await ctx.send('!!account')

@bot.command()
async def rank(ctx):
  await ctx.send('your range is top')


@bot.command()
async def loly(ctx,x):
   await ctx.send(x)

@bot.command()
async def er(ctx):
  await ctx.channel.send('!!account')

bot.run('Your token')