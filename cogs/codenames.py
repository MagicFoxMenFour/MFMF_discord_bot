import disnake
from disnake.ext import commands, tasks
from disnake import app_commands
from datetime import timedelta, datetime
from disnake.utils import get
import json
        
codenames_role=[1101100875709153300, 1101100794096394280, 1101100469205606431, 1101100394555375686, 1079791565586845707]
codenames_refund=[1079791565586845707, 1101100875709153300, 1101100794096394280]

class codenames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Модуль {} загружен".format(self.__class__.__name__))


    @commands.slash_command(description="Регистрация нового кодового слова")
    @commands.has_any_role(*codenames_role)
    async def codenames_create(self, ctx, пользователь: disnake.Member=commands.Param(description="Выбираете человека на которого оформляете кодовое слово"), 
                               дней: int=commands.Param(description="Введите сколько дней кодовое слово будет действительныйм"),
                               кодовое_слово: str=commands.Param(description="Кодовое слово"),
                               шаблон: str=commands.Param(description="Шаблон для редактирования"),
                               категория: str=commands.Param(description="Категория кодового слова", 
                                                             choices=["Бизнесы", "Организации округа ЛС", "Организации", "Услуги", "Прочее"])
                               ):
        time=datetime.now()
        time2 = time + timedelta(days=дней)
        time3 = time2.strftime("%Y%m%d")
        time4 = time2.strftime("%d.%m.%Y")
        if категория == "Бизнесы":
            embed1=disnake.Embed(
                    title="Зарегистрировано новое кодовое слово (Бизнесы)",
                    description=f"Шаблон действует до {time4}г. (МСК)",
                    color=0xc35de8,
            )
            embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
            embed1.add_field(name="Шаблон", value=f"{шаблон}", inline=False)
            embed1.add_field(name="Владелец", value=f"{пользователь.mention}", inline=False)
            embed1.add_field(name="Зарегистрировал", value=f"{ctx.author.mention}", inline=False)
            embed1.set_footer(text="MFMF")
            with open("public/codenames.json", "r") as file:
                data=json.load(file)
                insert= [i for i, d in enumerate(data["fields"]) if d.get("name") == "\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u0411\u0438\u0437\u043d\u0435\u0441\u044b\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac"][0]

                num2 = {
                    "name": f"{кодовое_слово}",
                    "value": f"```{шаблон}```",
                    "inline": "false",
                    "data": int(time3)
                }
            
                data["fields"].insert(insert+1, num2)
            with open("public/codenames.json", "w") as file:                        
                json.dump(data, file, indent=4)
                file.close()

            embed=disnake.Embed.from_dict(data)
            await ctx.send(embed=embed1)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)

        if категория == "Организации округа ЛС":
            embed1=disnake.Embed(
                    title="Зарегистрировано новое кодовое слово (Организации округа ЛС)",
                    description=f"Шаблон действует до {time4}г. (МСК)",
                    color=0xc35de8,
            )
            embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
            embed1.add_field(name="Шаблон", value=f"{шаблон}", inline=False)
            embed1.add_field(name="Владелец", value=f"{пользователь.mention}", inline=False)
            embed1.add_field(name="Зарегистрировал", value=f"{ctx.author.mention}", inline=False)
            embed1.set_footer(text="MFMF")
            with open("public/codenames.json", "r") as file:
                data=json.load(file)
                insert= [i for i, d in enumerate(data["fields"]) if d.get("name") == "\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438 \u043e\u043a\u0440\u0443\u0433\u0430 \u041b\u0421\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac"][0]

                num2 = {
                    "name": f"{кодовое_слово}",
                    "value": f"```{шаблон}```",
                    "inline": "false",
                    "data": int(time3)
                }
            
                data["fields"].insert(insert+1, num2)
            with open("public/codenames.json", "w") as file:                        
                json.dump(data, file, indent=4)
                file.close()

            embed=disnake.Embed.from_dict(data)
            await ctx.send(embed=embed1)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)

        if категория == "Организации":
            embed1=disnake.Embed(
                    title="Зарегистрировано новое кодовое слово (Организации))",
                    description=f"Шаблон действует до {time4}г. (МСК)",
                    color=0xc35de8,
            )
            embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
            embed1.add_field(name="Шаблон", value=f"{шаблон}", inline=False)
            embed1.add_field(name="Владелец", value=f"{пользователь.mention}", inline=False)
            embed1.add_field(name="Зарегистрировал", value=f"{ctx.author.mention}", inline=False)
            embed1.set_footer(text="MFMF")
            with open("public/codenames.json", "r") as file:
                data=json.load(file)
                insert= [i for i, d in enumerate(data["fields"]) if d.get("name") == "\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac"][0]

                num2 = {
                    "name": f"{кодовое_слово}",
                    "value": f"```{шаблон}```",
                    "inline": "false",
                    "data": int(time3)
                }
            
                data["fields"].insert(insert+1, num2)
            with open("public/codenames.json", "w") as file:                        
                json.dump(data, file, indent=4)
                file.close()

            embed=disnake.Embed.from_dict(data)
            await ctx.send(embed=embed1)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)

        if категория == "Услуги":
            embed1=disnake.Embed(
                    title="Зарегистрировано новое кодовое слово (Услуги)",
                    description=f"Шаблон действует до {time4}г. (МСК)",
                    color=0xc35de8,
            )
            embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
            embed1.add_field(name="Шаблон", value=f"{шаблон}", inline=False)
            embed1.add_field(name="Владелец", value=f"{пользователь.mention}", inline=False)
            embed1.add_field(name="Зарегистрировал", value=f"{ctx.author.mention}", inline=False)
            embed1.set_footer(text="MFMF")
            with open("public/codenames.json", "r") as file:
                data=json.load(file)
                insert= [i for i, d in enumerate(data["fields"]) if d.get("name") == "\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u0423\u0441\u043b\u0443\u0433\u0438\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac"][0]

                num2 = {
                    "name": f"{кодовое_слово}",
                    "value": f"```{шаблон}```",
                    "inline": "false",
                    "data": int(time3)
                }
            
                data["fields"].insert(insert+1, num2)
            with open("public/codenames.json", "w") as file:                        
                json.dump(data, file, indent=4)
                file.close()

            embed=disnake.Embed.from_dict(data)
            await ctx.send(embed=embed1)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)

        if категория == "Прочее":
            embed1=disnake.Embed(
                    title="Зарегистрировано новое кодовое слово (Прочее)",
                    description=f"Шаблон действует до {time4}г. (МСК)",
                    color=0xc35de8,
            )
            embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
            embed1.add_field(name="Шаблон", value=f"{шаблон}", inline=False)
            embed1.add_field(name="Владелец", value=f"{пользователь.mention}", inline=False)
            embed1.add_field(name="Зарегистрировал", value=f"{ctx.author.mention}", inline=False)
            embed1.set_footer(text="MFMF")
            with open("public/codenames.json", "r") as file:
                data=json.load(file)
                insert= [i for i, d in enumerate(data["fields"]) if d.get("name") == "\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u041f\u0440\u043e\u0447\u0435\u0435\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac\u25ac"][0]

                num2 = {
                    "name": f"{кодовое_слово}",
                    "value": f"```{шаблон}```",
                    "inline": "false",
                    "data": int(time3)
                }
            
                data["fields"].insert(insert+1, num2)
            with open("public/codenames.json", "w") as file:                        
                json.dump(data, file, indent=4)
                file.close()

            embed=disnake.Embed.from_dict(data)
            await ctx.send(embed=embed1)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)

    @commands.slash_command(description="Удаление кодового слова")
    @commands.has_any_role(*codenames_role)
    async def codenames_delete(self, ctx, кодовое_слово: str=commands.Param(description="Пишите название кодового слова, которое хотите удалить")):
          
        with open("public/codenames.json", "r") as file:
            data=json.load(file)
        
        embed1=disnake.Embed(
                    title="Кодовое слово было удалено",
                    description=f"",
                    color=0xc35de8,
        )
        embed1.add_field(name="Кодовое слово", value=f"{кодовое_слово}", inline=False)
        embed1.add_field(name="Удалил", value=f"{ctx.author.mention}", inline=False)
        embed1.set_footer(text="MFMF")
            
        insert=[f"{кодовое_слово}"]
        for element in data["fields"]:
            if element['name'] in insert:
                data['fields'].remove(element)

        with open("public/codenames.json", "w") as file:                        
            json.dump(data, file, indent=4)
            file.close()

        embed=disnake.Embed.from_dict(data)
        await ctx.send(embed=embed1)
        await self.bot.get_channel(1117051347674603530).send(embed=embed)

    @commands.slash_command(description="Сбрасывание всех кодовых слов (Без возврата!!! Все придется заного делать!)")
    @commands.has_any_role(*codenames_refund)
    async def refund(self, ctx):
            
            with open("public/codenames.json", "r") as file:
                                data=json.load(file)
                                data={"title": "Список актуальных кодовых слов",
                                    "color": 16705372,
                                    "thumbnail": {
                                        "url": "https://pixelbox.ru/wp-content/uploads/2021/09/anime-gif-discord-42.gif"
                                    },
                                    "fields": [
                                        {
                                            "name": "▬▬▬▬▬▬▬▬Бизнесы▬▬▬▬▬▬▬▬",
                                            "value": "",
                                            "inline": "false"
                                        },
                                        {
                                            "name": "▬▬▬▬▬▬▬▬Организации округа ЛС▬▬▬▬▬▬▬▬",
                                            "value": "",
                                            "inline": "false"
                                        },
                                        {
                                            "name": "▬▬▬▬▬▬▬▬Организации▬▬▬▬▬▬▬▬",
                                            "value": "",
                                            "inline": "false"
                                        },
                                        {
                                            "name": "▬▬▬▬▬▬▬▬Услуги▬▬▬▬▬▬▬▬",
                                            "value": "",
                                            "inline": "false"
                                        },
                                        {
                                            "name": "▬▬▬▬▬▬▬▬Прочее▬▬▬▬▬▬▬▬",
                                            "value": "",
                                            "inline": "false"
                                        }
                                    ],
                                    "footer": {
                                        "text": "Discord",
                                        "icon_url": "https://derpicdn.net/img/2020/2/23/2281534/large.png"
                                    }}
            with open("public/codenames.json", "w") as file:
                                        
                                json.dump(data, file, indent=4)
                                file.close()
            embed=disnake.Embed.from_dict(data)
            await self.bot.get_channel(1117051347674603530).send(embed=embed)
    

def setup(bot):
    bot.add_cog(codenames(bot))