import disnake
from disnake.ext import commands
from disnake import app_commands
import datetime
from typing import List

class Loggies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Модуль {} загружен".format(self.__class__.__name__))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        msg=f"{member.name} ({member.id}) зашел на сервер."
        await self.bot.get_channel(1094870503245750303).send(msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        msg=f"{member.name} ({member.id}) вышел из сервера."
        await self.bot.get_channel(1094870503245750303).send(msg)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        msg=f"Сообщение до изменений `{before.content}`\n" \
            f"Сообщение после изменений `{after.content}`"
        await self.bot.get_channel(1095308192789037127).send(msg)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        msg=f"Удаленное сообщение `{message.content}` от пользователя `{message.author}`\n"
        await self.bot.get_channel(1095308192789037127).send(msg)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
        if before.channel is None:
            msg=f"{member.display_name} перешел в канал {after.channel.mention}"
            await self.bot.get_channel(1095312445536473108).send(msg)
        elif after.channel is None:
            msg=f"{member.display_name} покинул канал {before.channel.mention}"
            await self.bot.get_channel(1095312445536473108).send(msg)
        elif before.channel != after.channel:
            msg=f"{member.display_name} перешел из канала {before.channel.mention} в канал {after.channel.mention}"
            await self.bot.get_channel(1095312445536473108).send(msg)

    @commands.command()
    async def guild(self, ctx):
        all=len(ctx.guild.members)
        members=len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        bots=len(list(filter(lambda m: m.bot, ctx.guild.members)))
        emoji= int()
        anim_emoji= int()
        for emoji in ctx.guild.emojis:
            if emoji.animated == True:
                anim_emoji += 1
            elif emoji.animated == False:
                emoji += 1
        online = 0
        idle = 0
        offline = 0
        dnd = 0

        text = 0
        voice = 0
        for member in ctx.guild.members:
            if str(member.status) == "online":
                online += 1  
            if str(member.status) == "idle":
                idle += 1 
            if str(member.status) == "offline":
                offline += 1 
            if str(member.status) == "dnd":
                dnd += 1 
        for channel in ctx.guild.channels:
            if str(channel.type) == "text":
                text += 1
            if str(channel.type) == "voice":
                voice += 1
        owner = ctx.guild.owner.mention

        await ctx.send(f"Всего - {all}\n"
                       f"Ботов - {bots}\n"
                       f"Людей - {members}\n"
                       f"Аним смайлов - {anim_emoji}\n"
                       f"Не аним смайлов - {emoji}\n"
                       f"Онлайн - {online}\n"
                       f"Оффлайн - {offline}\n"
                       f"Нет на месте - {dnd}\n"
                       f"Спят - {idle}\n"
                       f"Голосовых - {voice}\n"
                       f"Текстовых - {text}\n"
                       f"Владелец - {owner}\n"
                       )



def setup(bot):
    bot.add_cog(Loggies(bot))