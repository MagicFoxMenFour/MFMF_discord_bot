import disnake
import datetime
import requests
import random
import json, string
from disnake.ext import commands
from interactions import Intents
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
from cogs.radio import radio
from cogs.Admin import admin
from cogs.fraction_audit import fraction_audit
from cogs.Loggies import Loggies
from cogs.codenames import codenames
from cogs.task_loop import MyCog

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents().all())
intents = Intents.DEFAULT
intents.members = True
intents.message_content = True

bot.add_cog(radio(bot))
bot.add_cog(admin(bot))
bot.add_cog(fraction_audit(bot))
bot.add_cog(Loggies(bot))
bot.add_cog(codenames(bot))
bot.add_cog(MyCog(bot))

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Streaming(name="игру", url="https://www.twitch.tv/MagicFoxMEnFour"))
    print(f"Бот {bot.user} запустился и может начать работать")  

#Простой калькулятор
@bot.slash_command(description="Пишешь цифру, потом + или -, потом опять цифру")
async def calc(inter, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Не правильно делаешь."
    await inter.send(str(result))


@bot.command()
async def png(ctx):
    await ctx.message.delete()
    imag=Image.open("img/large.png")# Это фоновое изображение
    img=imag.resize((1162, 648))# Размеры фона
    img=img.convert("RGB")
    url=str(ctx.author.avatar)# Находим аватар автора
    response=requests.get(url, stream=True)
    response=Image.open(BytesIO(response.content))
    response=response.convert("RGB")# Переводим автар в RGBA 
    response=response.resize((400, 400), Image.ANTIALIAS)# Устанавляваем для аватара размеры и сглаживание

    img.paste(response, (700, 50))# Устанавливаем расположение аватара на фоне
    idraw=ImageDraw.Draw(img)
    
    name=ctx.author.name# Не важно
    tag=ctx.author.discriminator# Не важно
    headline=ImageFont.truetype("a_AssuanTitulStrDs.ttf", size=60)# Не важно
    undertext=ImageFont.truetype("a_AssuanTitulStrDs.ttf", size=35)# Не важно
    idraw.text((470, 500), f"{name}", font=headline)# Не важно
    idraw.text((470, 548), f"Welcome", font=undertext)# Не важно
    img.save("img/user_card.jpg")# Сохраняем полноценную картинку со всеми изминениями
    await ctx.send(file=disnake.File(fp="img/user_card.jpg"))# Выкладываем фото в чат

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1094636291674624000)
    role=disnake.utils.get(member.guild.roles, id=1094641277418614794)
    await member.add_roles (role)
    imag=Image.open("img/large.png")# Это фоновое изображение
    img=imag.resize((1162, 648))# Размеры фона
    img=img.convert("RGB")
    url=str(member.avatar)# Находим аватар автора
    response=requests.get(url, stream=True)
    response=Image.open(BytesIO(response.content))
    response=response.convert("RGB")# Переводим автар в RGBA 
    response=response.resize((400, 400), Image.ANTIALIAS)# Устанавляваем для аватара размеры и сглаживание

    img.paste(response, (700, 50))# Устанавливаем расположение аватара на фоне
    idraw=ImageDraw.Draw(img)
    
    name=member.name# Не важно
    tag=member.discriminator# Не важно
    headline=ImageFont.truetype("a_AssuanTitulStrDs.ttf", size=60)# Не важно
    undertext=ImageFont.truetype("a_AssuanTitulStrDs.ttf", size=35)# Не важно
    idraw.text((470, 500), f"{name}", font=headline)# Не важно
    idraw.text((470, 548), f"Приветствуем", font=undertext)# Не важно
    img.save("img/user_card.jpg")# Сохраняем полноценную картинку со всеми изминениями
    await channel.send(file=disnake.File(fp="img/user_card.jpg"))# Выкладываем фото в чат
    await channel.send(embed=disnake.Embed(description=f"Пользователь {member.name}, присоединился к нам!"))

@bot.slash_command(description='Игра "Орел или решка"')
async def game_orel_reshka(ctx):
    await ctx.send(random.choice(["Орел", "Решка"]))

@bot.slash_command(description="Угадай число")
async def game_chislo(ctx, chislo):
    ran=random.choice(["1", "2", "3", "4", "5"])
    ran1=ran
    if chislo != ran1:
        await ctx.send(f"Бот загадал число: {ran1}\n"
                       f"Вы загадали число: {chislo}\n"
                       f"Не угадал")
    else:
        await ctx.send(f"Бот загадал число: {ran1}\n"
                       f"Вы загадали число: {chislo}\n"
                       f"Угадал")

@bot.event
async def on_message(message):
    if  message.channel.id == 1095308192789037127:
        return
    if message.author.id == 1079710499068981278:
        return
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.content.split(" ")}.intersection(set(json.load(open("public/words.json")))) != set():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, а по губам тебе не дать?")
    await bot.process_commands(message)

@bot.slash_command(description="Информация о доступных командах")
async def help(ctx):
    embed=disnake.Embed(
        title="MFMF",
        description="Список доступных команд",
        color=0xc35de8,
        timestamp=datetime.datetime.now()
    )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_thumbnail(url="https://media.tenor.com/fuMORq4cNwgAAAAC/ladybug-miraculous.gif")
    embed.add_field(name="Использование команд:", value="@MFMF_bot `команда`", inline=False)
    embed.add_field(name="зайти", value="Когда вы будете в голосовом чате, то этой командой можно призвать бота к вам", inline=False)
    embed.add_field(name="выйти", value="Убирает бота из голосового чата", inline=False)
    embed.add_field(name="стоп", value="Остонавливает воспроизведение музыки в голосовом чате", inline=False)
    embed.add_field(name="играть", value="Включает музыку в голосовом чате", inline=False)
    embed.add_field(name="пауза", value="Ставит на паузу музыку", inline=False)
    embed.add_field(name="возобновить", value="Возобновляет воспроизведение музыки", inline=False)
    embed.add_field(name="guild", value="Выводит оинформацию о сервере", inline=False)
    embed.add_field(name="Использование следующих команд:", value="@MFMF_bot `команда` `@человек` с которым вы что то хотите сделать", inline=False)
    embed.add_field(name="kick", value="Выкидывает человека из дискорд сервера (нужны права админа)", inline=False)
    embed.add_field(name="ban", value="Банит человека на сервере (нужны права админа)", inline=False)
    embed.add_field(name="Со всеми осальными командами вы можете ознакомиться прописав в чате '/' (высветится список со всеми слеш командами)", value='', inline=False)
    await ctx.send(embed=embed)

bot.run("MTA3OTcxMDQ5OTA2ODk4MTI3OA.G4DJZo.LHjC5wZHl3zG1ZFizdB3OHU6L2Gggg9viYRhrE")