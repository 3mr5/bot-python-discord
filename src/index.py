import discord 
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description='This is a helper bot')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

@bot.command()
async def sum(ctx, num_one: int , num_two: int):
    await ctx.send(num_one + num_two)

@bot.command()
async def stadistics(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Statistics", 
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner})")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query = parse.urlencode({'search_query': search})
    html_content = requesy.urlopen('https://youtube.com/results?'+ query)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})'.html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


#events
@bot.event
async def on_ready():
    print('My bot is ready')
    await bot.change_presence(activity=discord.Streaming(name='Bots', url="http://www.twitch.tv/cometacos_14"))

bot.run('NjQ2OTAyMzczNTcwMTgzMTY4.XdX5JQ.nc4zfhBMqyustLLB5y5fmvhuIuo')
