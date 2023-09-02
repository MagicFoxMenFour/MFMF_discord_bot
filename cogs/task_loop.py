
import disnake
from disnake.ext import commands, tasks
from disnake import app_commands
from datetime import timedelta, datetime
from disnake.utils import get
import json

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=1.0)
    async def printer(self):
        time=datetime.now()
        time2 = time.strftime("%Y%m%d")
        channel = self.bot.get_channel(1117051347674603530)
        print(time2)
        with open("public/codenames.json", "r") as file:
            data=json.load(file)
            
            insert=int(time2)
            for element in data["fields"]:
                try:
                    if element["data"] <= insert:
                        embed1=disnake.Embed(
                                    title="У кодового слова закончилась подписка",
                                    description=f"",
                                    color=0xc35de8,
                        )
                        embed1.add_field(name="Кодовое слово", value=element["name"], inline=False)
                        embed1.add_field(name="Шаблон", value=element["value"], inline=False)
                        embed1.set_footer(text="MFMF")
                        embed=disnake.Embed.from_dict(data)

                        data["fields"].remove(element)
                        with open("public/codenames.json", "w") as file:                        
                            json.dump(data, file, indent=4)

                        await channel.send(embed=embed1)
                        await self.bot.get_channel(1117051347674603530).send(embed=embed)
                except KeyError:
                    continue
                
        with open("public/codenames.json", "w") as file:                        
            json.dump(data, file, indent=4)
            file.close()

    @printer.before_loop
    async def before_printer(self):
        print('Запущена автоматическая проверка кодовых слов')
        await self.bot.wait_until_ready()
        
def setup(bot):
    bot.add_cog(MyCog(bot))