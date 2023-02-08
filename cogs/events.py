from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(events(bot))
