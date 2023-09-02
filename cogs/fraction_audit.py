import disnake
from disnake.ext import commands
from disnake import app_commands
import datetime
from disnake.utils import get
import json

bot = commands.Bot

fraction_audit_roles=[1101549407398268958, 1101100469205606431, 1101100469205606431, 1101100875709153300, 1079791565586845707]
fraction_audit_perevod_roles=[1101100875709153300, 1101100794096394280, 1101100469205606431, 1101100394555375686, 1101100312716128276, 1101550231105060997, 1101549898542882826, 1079791565586845707]
fraction_number_sobes_roles=[1101100875709153300, 1101100794096394280, 1101100469205606431, 1101100394555375686, 1101100312716128276, 1101550231105060997, 1101549898542882826, 1079791565586845707]
fraction_medcard_give_roles=[1105809361420431362, 1101100469205606431, 1101100794096394280, 1101100794096394280, 1079791565586845707]

class fraction_audit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Модуль {} загружен".format(self.__class__.__name__))
        

    @commands.slash_command(description="выбирает привет или пока")
    async def choice(ctx, choice:str=commands.Param(choices=["Привет", "Пока"])):
        if choice == "Привет":
            await ctx.send(f"Ты выбрал: `{choice}`")
           
        if choice == "Пока":
            await ctx.send(f"Ты проиграл: `{choice}`")
    
    @commands.slash_command(description="Для принятия человека во фракцию")
    @commands.has_any_role(*fraction_audit_roles)
    async def fraction_audit_newinvite(self, ctx, пользователь:disnake.Member=commands.Param(description="Выбираете человека, которого хотите принять во фракцию"),
                                   ник:str=commands.Param(description="Пишите имя и фамилию человека как в паспорте"), 
                                   паспорт: int=commands.Param(description="Вводите номер паспорта"), 
                                   фото: disnake.Attachment=commands.Param(description="Вставляете скриншот паспорта")):
        t=datetime.datetime.now()
        timestamp=t.strftime("%d.%m.%Yг.")
        role=get(ctx.guild.roles, id=1095764024802680924)
        role2=get(ctx.guild.roles, id=1101549737867497492)
        channel = self.bot.get_channel(1096032652743688262)
        with open("public/members.json", "r") as file:
                    data=json.load(file)
        try:
            if data[str(пользователь.id)]["PASSPORT"] == str(паспорт):
                await ctx.send (f"{ctx.author.mention} попытался принять человека, который находится в черном списке.")
            else:    
                await фото.save("img/invite.jpg") 
                await пользователь.edit(nick=f"1 | {ник}")
                await пользователь.add_roles(role)
                await пользователь.add_roles(role2)
                await ctx.send(f"{пользователь.mention} ({ник}) ({паспорт}) принят в организацию Weazel News на должность {role.mention} по собеседованию. Дата: {timestamp}")
                                
                with open("public/sobes.json", "r") as file:
                            data=json.load(file)
                            data[str(ctx.guild.id)]["NUMBER_SOBES"] +=1
                                                                
                with open("public/sobes.json", "w") as file:
                                    
                            json.dump(data, file, indent=4)
                            file.close()
                                
                await channel.send(f"1. {ctx.author.mention}\n"
                                        f"2. {ник}\n"
                                        f"3. {timestamp}\n"  
                                        f"4. Прошел \n"
                                        f'5. {data[str(ctx.guild.id)]["NUMBER_SOBES"] -1}\n',
                                        file=disnake.File("img/invite.jpg"))
        except KeyError:
                await фото.save("img/invite.jpg") 
                await пользователь.edit(nick=f"1 | {ник}")
                await пользователь.add_roles(role)
                await ctx.send(f"{пользователь.mention} ({ник}) ({паспорт}) принят в организацию Weazel News на должность {role.mention} по собеседованию. Дата: {timestamp}")
                                
                with open("public/sobes.json", "r") as file:
                            data=json.load(file)
                            data[str(ctx.guild.id)]["NUMBER_SOBES"] +=1
                                                                
                with open("public/sobes.json", "w") as file:
                                    
                            json.dump(data, file, indent=4)
                            file.close()
                                
                await channel.send(f"1. {ctx.author.mention}\n"
                                        f"2. {ник}\n"
                                        f"3. {timestamp}\n"  
                                        f"4. Прошел \n"
                                        f'5. {data[str(ctx.guild.id)]["NUMBER_SOBES"] -1}\n',
                                        file=disnake.File("img/invite.jpg"))

    @fraction_audit_newinvite.error
    async def newinvite_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете принимать людей во фракцию.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Оставить отчет по собеседованию")
    @commands.has_any_role(*fraction_audit_roles)
    async def fraction_audit_sobes(self, ctx, ник:str=commands.Param(description="Пишите имя и фамилию человека как в паспорте"), 
                                   статус: str=commands.Param(description="Гражданин прошел собеседование?", choices=["Прошел собеседование", "Не прошел собеседование"]), 
                                   фото: disnake.Attachment=commands.Param(description="Вставляете скриншот паспорта")):
                                   
        t=datetime.datetime.now()
        timestamp=t.strftime("%d.%m.%Yг.")
        channel = self.bot.get_channel(1096032652743688262)
        await фото.save("img/invite.jpg") 
        if статус == "Прошел собеседование":
            await channel.send(f"1. {ctx.author.mention}\n"
                            f"2. {ник}\n"
                            f"3. {timestamp}\n"  
                            f"4. Прошел \n"
                            f"5. \n",
                            file=disnake.File("img/invite.jpg"))
        if статус == "Не прошел собеседование":
            await channel.send(f"1. {ctx.author.mention}\n"
                            f"2. {ник}\n"
                            f"3. {timestamp}\n"  
                            f"4. Не прошел \n"
                            f"5. \n",
                            file=disnake.File("img/invite.jpg"))
    
    @fraction_audit_sobes.error
    async def sobes_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете оставлять отчет.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)
    
    @commands.slash_command(description="Увольнение человека")
    @commands.has_any_role(*fraction_audit_roles)
    async def fraction_audit_uval(self, ctx, пользователь:disnake.Member=commands.Param(description="Выбираете пользовотеля которого хотите уволить"), 
                              причина:str=commands.Param(description="Пишите причину по которой его увольняете"),
                              причина_чс: str=commands.Param(description="Вводите причину занесения в черный список. (Если не собираетесь вносить в ЧС, то вводите что угодно)"),
                              чс: str=commands.Param(description="Вносить в черный список?", choices=["С занесением в черный список", "Без занесения в черный список"]),
                              паспорт: int=commands.Param(description="Пишите номер паспорта увольниемого человека")
                              ):
        t=datetime.datetime.now()
        time=t.strftime("%d.%m.%Yг.")
        nik=пользователь.nick[4:]
        channel = self.bot.get_channel(1102201266999939263)
        channel_audit=self.bot.get_channel(1117053976626614272)
        if чс == "С занесением в черный список":
            await пользователь.edit(nick=f"{nik}")
            await пользователь.edit(roles=[]) 
            await ctx.send(f"{пользователь.mention} ({nik}) уволен из организации Weazel News. По причине: {причина}. Дата: {time}")
            await channel.send(f"1. {пользователь.mention}\n"
                            f"2. {nik}\n"
                            f"3. {паспорт}\n"  
                            f"4. {причина_чс} \n"
                            f"(( В черный список занес(ла): {ctx.author.nick} ({ctx.author.mention}) )) ")
            with open(f"public/members.json", "r") as file:
                data=json.load(file)
                data[str(пользователь.id)] = {
                    "PASSPORT": str(паспорт)
                                            }
            with open("public/members.json", "w") as file:
                
                json.dump(data, file, indent=4)
                file.close()  

        if чс == "Без занесения в черный список":
            await пользователь.edit(nick=f"{nik}")
            await пользователь.edit(roles=[]) 
            await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) уволен из организации Weazel News. По причине: {причина}. Дата: {time}")
    
    @fraction_audit_uval.error
    async def uval_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете увольнять людей из фракции.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Перевести или принять человека в дирекцию")
    @commands.has_any_role(*fraction_audit_perevod_roles)
    async def fraction_audit_perevod(self, ctx, пользователь:disnake.Member=commands.Param(description="Выбираете пользовотеля которого хотите принять или перевести"), 
                                операция: str=commands.Param(choices=["Перевести в дирекцию", "Вывести из состава дирекции"], description="Выбираете действие"),
                                причина:str=commands.Param(description="Пишите причину по которой его увольняете"),
                                дирекция: str=commands.Param(choices=["Кадры", "Публицистическое вещание", "Информационные программы", "Социальные программы", "Телевидение", "Спецпроекты"], description="Выбираете дирекцию в которую вы переводите сотрудника")):
        t=datetime.datetime.now()
        time=t.strftime("%d.%m.%Yг.")
        if операция == "Перевести в дирекцию":
            if дирекция == "Кадры":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"Cт.Кадры | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101549407398268958)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Кадры. По причине: {причина}. Дата: {time}")
            if дирекция == "Публицистическое вещание":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"ПВ | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101599477162311700)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Публицистическое вещание. По причине: {причина}. Дата: {time}")
            if дирекция == "Информационные программы":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"ИП | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101599593742999666)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Информационные программы. По причине: {причина}. Дата: {time}")
            if дирекция == "Социальные программы":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"СП | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101599776115544114)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Социальные программы. По причине: {причина}. Дата: {time}")
            if дирекция == "Телевидение":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"ТВ | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101599838308663337)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Телевидение. По причине: {причина}. Дата: {time}")
            if дирекция == "Спецпроекты":
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"Спец | {nik}")
                await пользователь.add_roles(get(ctx.guild.roles, id=1101599966637592698)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) переведен в дирекцию Спецпроекты. По причине: {причина}. Дата: {time}")
        if операция == "Вывести из состава дирекции":
            if дирекция == "Кадры":
                nik=пользователь.nick[8:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101549407398268958)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Кадры. По причине: {причина}. Дата: {time}")
            if дирекция == "Публицистическое вещание":
                nik=пользователь.nick[5:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101599477162311700)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Публицистическое вещание. По причине: {причина}. Дата: {time}")
            if дирекция == "Информационные программы":
                nik=пользователь.nick[5:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101599593742999666)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Информационные программы. По причине: {причина}. Дата: {time}")
            if дирекция == "Социальные программы":
                nik=пользователь.nick[5:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101599776115544114)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Социальные программы. По причине: {причина}. Дата: {time}")
            if дирекция == "Телевидение":
                nik=пользователь.nick[5:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101599838308663337)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Телевидение. По причине: {причина}. Дата: {time}")
            if дирекция == "Спецпроекты":
                nik=пользователь.nick[7:]
                await пользователь.edit(nick=f"WN | {nik}")
                await пользователь.remove_roles(get(ctx.guild.roles, id=1101599966637592698)) 
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) выведен из состава дирекции Спецпроекты. По причине: {причина}. Дата: {time}")

    @fraction_audit_perevod.error
    async def perevod_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете принимать, переводить или увольнять людей внутри дирекции.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Выдача предупреждения по мед.карте")
    @commands.has_any_role(*fraction_medcard_give_roles)
    async def fraction_medcard_give(self, ctx, пользователь:disnake.Member=commands.Param(description="Выбираете пользователя у которого просрочена медюкарта"), 
                                    причина:str=commands.Param(description="Пишите причину выдачи предупреждения")):
        member=disnake.utils.get(ctx.guild.members, id=1079710499068981278)
        t=datetime.datetime.now()
        time=t.strftime("%d.%m.%Yг. в %H:%M")
        
        embed=disnake.Embed(
            title="Вам выдоно предупреждение по мед.карте!",
            description="В течении 48 часов вам необходимо загрузить отчет по медкарте",
            color=0x8f509d,)
        embed.set_thumbnail(url="")
        embed.add_field(name="Причина", value=f"{причина}", inline=False)
        embed.add_field(name="Заполните отчет", value="https://youtu.be/Kn4Y-yCpsXo", inline=False)
        embed.add_field(name="Дата выдачи предупреждения", value=f"{time} по МСК", inline=False)
        embed.add_field(name="Выдал(а) предупреждение", value=f"{ctx.author.nick} ({ctx.author.mention})", inline=False)
        embed.set_footer(text=member.display_name, icon_url=member.avatar)
        await пользователь.send(embed=embed)

        embed1=disnake.Embed(
            title="Выдано предупреждение по мед.карте",
            description="Сотруднику выдано предупреждение по медкарте!",
            color=0x8f509d,)
        embed1.set_thumbnail(url="")
        embed1.add_field(name="Предупреждение получил(а)", value=f"{пользователь.mention}", inline=False)
        embed1.add_field(name="Причина", value=f"{причина}", inline=False)
        embed1.add_field(name="Заполните отчет", value="https://youtu.be/Kn4Y-yCpsXo", inline=False)
        embed1.add_field(name="Дата выдачи предупреждения", value=f"{time} по МСК", inline=False)
        embed1.add_field(name="Выдал(а) предупреждение", value=f"{ctx.author.nick} ({ctx.author.mention})", inline=False)
        embed.set_footer(icon_url=member.avatar, text="MFMF_bot (r)")
        await self.bot.get_channel(1117052905443295252).send(embed=embed1)

    @fraction_medcard_give.error
    async def medcard_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете производить действия с мед. картами.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Сбрасывание нумерации собеседований")
    @commands.has_any_role(*fraction_number_sobes_roles)
    async def fraction_number_sobes(self, ctx):
        with open("public/sobes.json", "r") as file:
            data=json.load(file)
            data[str(ctx.guild.id)] = {
                "NUMBER_SOBES": 1
                                        }
        with open("public/sobes.json", "w") as file:
                
            json.dump(data, file, indent=4)
            file.close()
        channel = self.bot.get_channel(1096032652743688262)
        await channel.send("=============================================================\n"
                           f"{ctx.author.mention} сбросил нумерацию собеседований\n"
                           "=============================================================")

    @fraction_number_sobes.error
    async def number_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете сбрасывать нумерацию собеседований.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Повышение человека")
    @commands.has_any_role(*fraction_audit_roles)
    async def fraction_audit_rang(self, ctx, пользователь:disnake.Member=commands.Param(description="Выбираете пользователя с которым вы хотите произвести действие"), 
                              операция: str=commands.Param(choices=["Повысить сотрудника", "Понизить сотрудника", "Назначить на должность", "Снять с должности"], description="Выбираете действие"),
                              причина: str=commands.Param(description="Пишите по какой причине то или иное действие"), 
                              ранг:disnake.Role=commands.Param(description="Выбираете роль которую вы хотите дать"), 
                              номер_указа: int=False):
        t=datetime.datetime.now()
        timestamp=t.strftime("%d.%m.%Yг.")
        if операция == "Повысить сотрудника":
            if ранг == get(ctx.guild.roles, id=1095954036735348788):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"2 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095764024802680924))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095764222065004554):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"3 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095954036735348788))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
                
            if ранг == get(ctx.guild.roles, id=1095962149710462976):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"4 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095764222065004554))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095962910506876958):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"5 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095962149710462976))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963070305677333):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"6 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095962910506876958))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963137888497695):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"7 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963070305677333))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963215453761656):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"8 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963137888497695))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963275415523408):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"9 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963215453761656))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) повышен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
        if операция == "Понизить сотрудника":
            if ранг == get(ctx.guild.roles, id=1095963215453761656):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"8 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963275415523408))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963137888497695):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"7 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963215453761656))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095963070305677333):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"6 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963137888497695))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095962910506876958):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"5 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095963070305677333))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095962149710462976):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"4 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095962910506876958))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095764222065004554):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"3 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095962149710462976))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095954036735348788):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"2 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095764222065004554))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1095764024802680924):
                nik=пользователь.nick[4:]
                await пользователь.edit(nick=f"1 | {nik}")
                await пользователь.add_roles(ранг)
                await пользователь.remove_roles(get(ctx.guild.roles, id=1095954036735348788))
                await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) понижен на должность {ранг.mention}. По причине: {причина}. Дата: {timestamp}")
        if операция == "Назначить на должность":
            if ранг == get(ctx.guild.roles, id=1101100312716128276):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100394555375686):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100875709153300):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100469205606431):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=11101100794096394280):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) назначен на должность {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
        if операция == "Снять с должности":
            if ранг == get(ctx.guild.roles, id=1101100312716128276):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100394555375686):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100469205606431):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100794096394280):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")
            if ранг == get(ctx.guild.roles, id=1101100875709153300):
                if номер_указа == False:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} по причине: {причина}. Дата: {timestamp}")
                else:
                    nik=пользователь.nick[4:]
                    await self.bot.get_channel(1117053976626614272).send(f"{пользователь.mention} ({nik}) снят с должности {ранг.mention} согласно указу: №{номер_указа}. Дата: {timestamp}")

    @fraction_audit_rang.error
    async def rang_error(self, ctx: disnake.Interaction, error):
        embed=disnake.Embed(
            title="",
            description="",
            color=0xc35de8
        )
        embed.add_field(name="Ошибка прав", value="Вы не можете повышать или понижать человека в должности.", inline=False)

        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(fraction_audit(bot))