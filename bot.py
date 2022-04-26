import discord
import asyncio
import random
import datetime
import re 
from pypresence import Presence
from time import time
from discord.ext import commands
from discord.utils import get
from discord import Embed
from discord.ext import tasks
from aiohttp import ClientSession
from typing import Optional






bot=commands.Bot(command_prefix = 'b!')
bot.remove_command('help')



@bot.event
async def on_ready():
    print("Bot is running!")
    activity=discord.Streaming(name=f'я на {len(bot.guilds)} серверах! | b!help', url="https://youtu.be/dQw4w9WgXcQ")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        title='Приветствие',
        description=f'привет! Меня добавили на этот сервер!\n⚙️ чтобы посмотреть на все мои команды то напиши - ```{ctx.prefix}help```\n[добавить бота](https://discord.com/oauth2/authorize?client_id=948551023142785044&scope=bot&permissions=8) ',
        color=0x546e7a
        )
    await guild.text_channels[0].send(embed=embed)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      error_embed = discord.Embed(
     title="❌ | 0шибочка", 
     description="в боте нет такой команды!",
     color=0x546e7a
                    
                    )
                    
    await ctx.send(embed = error_embed)
    
@bot.command()
async def toserver(ctx):
    nb = 783070284152045621
    if ctx.author.id == nb:
        for guild in bot.guilds:
            await ctx.send(guild.name)
            guild = bot.get_guild(guild.id)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
            await ctx.send(invite)
    else:
        embed = discord.Embed(description=f'{ctx.author.mention} данной команды не существует', color = 0x00008b)
        await ctx.send(embed=embed)
        




  

      


 
     
# HELP
 
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="❗| Помощь",
        description=f"```Префикс бота - {ctx.prefix}```\n \n**Основное**\n{ctx.prefix}help\n{ctx.prefix}звонить <вопрос>\n{ctx.prefix}газета\n{ctx.prefix}лаборатория_help\n{ctx.prefix}рыгание\n{ctx.prefix}сказать\n{ctx.prefix}бить\n{ctx.prefix}пьет\n{ctx.prefix}еда\n{ctx.prefix}стул\n \n **Другое**\n{ctx.prefix}infobot\n{ctx.prefix}invite",
        color=0x546e7a
        
    )
    await ctx.send(embed=embed)
    


# [here](your_link_goes_here)



    
# ЛАБОРАТОРИЯ
    
    
@bot.command(aliases=['Лаборатория', 'лаборатория_help', 'Лаборатория_help'])
async def лаборатория(ctx):
    embed = discord.Embed(
        title=f"🌠 | Лаборатория help",
        description="все зелья: желтый, зеленый, голубой, фиолетовый, синий\nпример команды: b!желтый_зеленый\nнекоторые команды не работают❗",
        color=0x546e7a
        
    )
    await ctx.send(embed=embed)
    

    
    

@bot.command(aliases=['Желтый_зеленый', 'Желтый_Зеленый', 'Жёлтый_зеленый', 'Жёлтый_Зелёный', 'жёлтый_зелёный', 'Зеленый_Желтый', 'Зеленый_желтый', 'зелёный_жёлтый', 'Зелёный_Жёлтый'])
async def желтый_зеленый(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951197547169448087/20220309_221752.gif")
    

    
@bot.command(aliases=['Желтый_голубой', 'Желтый_Голубой', 'желтый_Голубой', 'голубой_Желтый', 'Голубой_желтый', 'Голубой_Желтый'])
async def желтый_голубой(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951202476315533322/20220309_223745.gif")

    
@bot.command(aliases=['Желтый_Фиолетовый', 'желтый_Фиолетовый', 'Желтый_фиолетовый', 'Фиолетовый_Желтый', 'фиолетовый_желтый', 'фиолетовый_Желтый'])
async def желтый_фиолетовый(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951203440002990130/20220309_223807.gif")

    
@bot.command(aliases=['Желтый_Синий', 'желтый_Синий', 'Желтый_синий', 'Синий_Желтый', 'синий_желтый', 'синий_Желтый'])
async def желтый_синий(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951205027396083742/20220309_224812.gif")
    
      
@bot.command(aliases=['зеленый_Голубой', 'Зеленый_голубой', 'Зеленый_Голубой', 'голубой_зеленый', 'Голубой_зеленый', 'Голубой_Зеленый'])
async def зеленый_голубой(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951207281960288266/20220309_225713.gif")
    

@bot.command(aliases=['зеленый_Фиолетовый', 'Зеленый_фиолетовый', 'Зеленый_Фиолетовый', 'фиолетовый_зеленый', 'Фиолетовый_зеленый', 'Фиолетовый_Зеленый'])
async def зеленый_фиолетовый(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951207281960288266/20220309_225713.gif")
    

@bot.command(aliases=['зеленый_Синий', 'Зеленый_синий', 'Зеленый_Синий', 'синий_зеленый', 'Синий_зеленый', 'Синий_Зеленый'])
async def зеленый_синий(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/951211565242281994/20220309_231421.gif")
    

@bot.command(aliases=['фиолетовый_Синий', 'Фиолетовый_синий', 'Фиолетовый_Синий', 'синий_фиолетовый', 'Синий_фиолетовый', 'Синий_Фиолетовый'])
async def фиолетовый_синий(ctx):
    await ctx.send(" https://media.discordapp.net/attachments/785041826959720458/951211565242281994/20220309_231421.gif")
    

# ДРУГИЕ КОМАНДЫ

@bot.command(aliases=['Звонить', 'позвонить', 'Позвонить'])
async def звонить(ctx, *, question):
  responses = [
  discord.Embed(title=f'ваш вопрос: {question}\n \n*вы звоните Бену*\nБен отвечает:\n \n```Yes```'),
  discord.Embed(title=f'ваш вопрос: {question}\n \n*вы звоните Бену*\nБен отвечает:\n \n```No```'),
  discord.Embed(title=f'ваш вопрос: {question}\n \n*вы звоните Бену*\nБен отвечает:\n \n```xoxoxo```'),
  discord.Embed(title=f'*ваш вопрос: {question}\n \nвы звоните Бену*\nБен отвечает:\n \n```be```'),
  discord.Embed(title=f'*ваш вопрос: {question}\n \nБен не отвечает*'),


  
  
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'', embed=responses)

@bot.command(aliases=['газета', 'гозета', 'Гозета'])
async def Газета(ctx, *, question):
  responses = [
  discord.Embed(title='Бен отвечает:\n```La-la-la-la```'),
  discord.Embed(title='Бен отвечает:\nпшш'),
  
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'', embed=responses)
  
  

  
@bot.command(aliases=['Стул'])
async def стул(ctx):
    await ctx.send("https://media.discordapp.net/attachments/785041826959720458/949677367574528040/20220305_173752.gif")

@bot.command(aliases=['Рыгание', 'отрыжка', 'Отрыжка'])
async def рыгание(ctx):
    await ctx.send("https://media.discordapp.net/attachments/944675354407235656/949335094353596426/20220304_185753.gif")


@bot.command(name='сказать')
async def Сказать(ctx, *, msg=None):
    if msg is not None:
        await ctx.send(msg)
        await ctx.message.delete()
     

    


@bot.command(aliases=['Пьет', 'вино', 'Вино'])
async def пьет(ctx):
    await ctx.send("https://media.discordapp.net/attachments/944675354407235656/949331175690874950/20220304_183854.gif")
    



    
@bot.command(aliases=['Бить'])
async def бить(ctx):
    await ctx.send("https://media.discordapp.net/attachments/944675354407235656/949338346012934215/20220304_191116.gif")
    
@bot.command(aliases=['Invite', 'Инвайт', 'инвайт'])
async def invite(ctx):
    embed = discord.Embed(
        title="🔔| Инвайт",
        description="[✨ ссылка на бота](https://discord.com/oauth2/authorize?client_id=948551023142785044&scope=bot&permissions=8)\n[🔗Сервер бота](https://discord.gg/HFa54X7wcx)",
        color=0x546e7a
        
    )
    await ctx.send(embed=embed)
    
    



 
@bot.command(aliases=['Еда'])
async def еда(ctx):
    await ctx.send("https://media.discordapp.net/attachments/943799479801376768/949589022928408606/20220305_114640.gif")
    
    
@bot.command(aliases = ['botinfo'])
async def infobot(ctx):
    embed = discord.Embed(
        title="👀 | Информация о боте",
        description=f"создатель бота - NB#0001\nязык программирования - Python 3 🐍\n🥶 мой пинг - {round(bot.latency * 1000)}ms\nдата создание бота - 2 марта\n \nколичество серверов - **{len(bot.guilds)}**\n \n[поддержать разработчика](https://www.donationalerts.com/r/nb228)",
        color=0x546e7a
        
    )
    await ctx.send(embed=embed)
    




    
bot.run("OTQ4NTUxMDIzMTQyNzg1MDQ0.Yh9c-w.0rUsBej9Pd1M2x3KggTqUBZ6isY")