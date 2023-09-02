import disnake
from disnake.ext import commands
from disnake import app_commands
from disnake import FFmpegPCMAudio
from disnake.utils import get

class radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Модуль {} загружен".format(self.__class__.__name__))

    #Бот заходит в тот голосовой чат в котором находится отправитель команды, 
    #если отправитель не в голосовом чате, то бот говорит об этом
    @commands.command()
    async def зайти(self, ctx):
        await ctx.message.delete()
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send(f"{ctx.author.mention} подключись к голосому чату сначало!")

    #Бот выходит из голосового чата или уведомляет, что его там нету
    @commands.command(pass_context = True)
    async def выйти(self, ctx):
        await ctx.message.delete()
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()

        else:
            await ctx.send("Я не в голосовом чате")

    #Остонавливает воспроизведение музыки в голосовом чате
    @commands.command()
    async def стоп(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.stop()

    #Возобновляет воспроизведение музыки
    @commands.command()
    async def возобновить(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.resume()

    #Ставит на паузу музыку
    @commands.command()
    async def пауза(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.pause()

    #Включает музыку в голосовом чате
    @commands.command()
    async def play1(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        voice1 = server.voice_client
        sourse = FFmpegPCMAudio("Che_za_urodi.wav")
        voice1.play(sourse)

    @commands.command()
    async def играть(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        player = server.voice_client
        player.play(FFmpegPCMAudio("https://everhoof.ru/320?t=1678287348208"))


def setup(bot):
    bot.add_cog(radio(bot))