import disnake
from disnake.ext import commands
from disnake import app_commands
from disnake.utils import get

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Модуль {} загружен".format(self.__class__.__name__))
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: disnake.Member, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f"Пользователь {member} был кикнут из сервера")

    @kick.error
    async def clear_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете кикать людей.", inline=False)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: disnake.Member, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f"Пользователь {member} был забанен")

    @ban.error
    async def clear_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете банить людей.", inline=False)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Выбираешь команду и пишешь сколько сообщений нужно удалить")
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount : int):
        await ctx.channel.purge(limit = int(amount))
        await ctx.send(f"{ctx.author.mention} очистил последние {amount} сообщений!")

    @clear.error
    async def clear_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете очищать сообщения.", inline=False)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(admin(bot))